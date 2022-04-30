import random
from transformers import set_seed
from myutils import Configs, auto_create_model, auto_get_dataset, auto_get_tag_names, auto_get_tokenizer, dataset_map_raw2ner, get_ner_evaluation
from mytrainer import NERTrainer
from transformers import AdamW
import torch
from torch.utils.data import DataLoader
import torch.nn.functional as F
import numpy as np

from ner_models import INERModel

def main():
    config = Configs.parse_from_argv()

    set_seed(config.random_seed)

    raw_dataset = auto_get_dataset(config)
    
    if config.few_shot:
        raw_dataset["train"] = raw_dataset["train"].shuffle(2333).select(list(range(int(len(raw_dataset["train"]) * config.few_shot))))
    
    tokenizer = auto_get_tokenizer(config)
    model : INERModel = auto_create_model(config, tokenizer).cuda()
    ner_dataset = raw_dataset.map(lambda x : dataset_map_raw2ner(tokenizer, x), batched=True)
    ner_dataset.set_format('torch', columns=NERTrainer.NER_DATA_COLUMNS)

    optimizer = AdamW(model.parameters(), lr=config.ner_lr, weight_decay=config.ner_weight_decay)
    trainer = NERTrainer(model, 
                        optimizer=optimizer, 
                        warmup_ratio=config.warmup_ratio,
                        label_smooth_factor=config.label_smooth_factor,
                        clip_grad_norm=config.clip_grad_norm,
                        grad_acc=config.grad_acc)
    tag_names = auto_get_tag_names(config)
    metric_eval = get_ner_evaluation()
    
    test_loader = DataLoader(ner_dataset["test"], batch_size=config.batch_size, pin_memory=True)
    def eval_function(metrics_data : dict):
        with torch.no_grad():
            y_pred = []
            y_true = []
            for batch in test_loader:
                batch_gpu = {
                    "input_ids" : batch["input_ids"].cuda(),
                    "attention_mask" : batch["attention_mask"].cuda(),
                    "tags" : batch["tags"].cuda(),
                    "length" : batch["length"].cuda()
                }
                decoded = model.decode(**batch_gpu)     #[batch_size, seq_length]
                y_pred.append(decoded)
                y_true.append(batch["tags"])

            if isinstance(y_pred[0], torch.Tensor):
                y_pred = [p.contiguous().view(-1) for p in y_pred]
            elif isinstance(y_pred[0], list):
                y_pred = [sum(p, []) for p in y_pred]
              #  y_pred = np.concatenate(y_pred)
            else:
                raise RuntimeError("Unkown decoded type")

            y_true = torch.cat(y_true).detach().cpu()

            true_predictions = [
                [tag_names[p] for (p, l) in zip(prediction, label) if l != -100]
                for prediction, label in zip(y_pred, y_true)
            ]
            true_labels = [
                [tag_names[l] for (p, l) in zip(prediction, label) if l != -100]
                for prediction, label in zip(y_pred, y_true)
            ]
            results = metric_eval.compute(predictions=true_predictions, references=true_labels)
            metrics_data.update({
                "f1": results["overall_f1"],
                "accuracy": results["overall_accuracy"],
            })
            print(metrics_data)
            return metrics_data
        
    trainer.train(config.ner_epoches, DataLoader(ner_dataset["train"], batch_size=config.batch_size, pin_memory=True), eval_function)
    

if __name__ == "__main__":
    main()

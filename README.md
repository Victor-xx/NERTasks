# NERTasks

# Contents
## [What's It?](#0)
## [1. Requrements](#1)
## [2. Install Dependencies](#2)
## [3. How To Prepare Datasets](#3)
## [4. Experiments](#4)
### [&nbsp; 4.1 Hyper Parameters](#4_1)
### [&nbsp; 4.2 Model Parameters](#4_2)
### [&nbsp; 4.3 Results](#4_3)
## [5. Acknowledgement And Citations](#5)
### [&nbsp; 5.1 People And Orgnizations](#5_1)
### [&nbsp; 5.2 Third-Party Libraries](#5_2)
### [&nbsp; 5.3 Papers](#5_3) 

<p id="0"> </p>

# What's It? 

<h4><b> A simple NER framework. </b> </h4>

It implements:

<table>
<thead>
<tr><td></td><td>Item</td><td>Source</td></tr>
</thred>
<tbody>
<tr><td rowspan="8">Models</td><td></td></tr>
    <tr><td>BiLSTM-Linear</td><td></td></tr>
    <tr><td>BiLSTM-Linear-CRF</td><td><a href="https://arxiv.org/abs/1603.01360">Neural Architectures for Named Entity Recognition</a></td></tr>
    <tr><td>BERT-Linear</td><td></td></tr>
    <tr><td>BERT-Linear-CRF</td><td></td></tr>
    <tr><td>BERT-BiLSTM-Linear</td><td></td></tr>
    <tr><td>BERT-BiLSTM-Linear-CRF</td><td></td></tr>
    <tr><td>BERT(Prompt)</td><td><a href="https://arxiv.org/abs/2109.13532">Template-free Prompt Tuning for Few-shot NER</a></td></tr>
<tr><td rowspan="4">Datasets</td></tr>
    <tr><td>CoNLL2003</td><td><a href="https://github.com/yuanxiaosc/BERT-for-Sequence-Labeling-and-Text-Classification/tree/master/data/CoNLL2003_NER">
yuanxiaosc/BERT-for-Sequence-Labeling-and-Text-Classification</a></td></tr>
    <tr><td>OntoNotes5</td><td><a href="https://catalog.ldc.upenn.edu/LDC2013T19">LDC2013T19</a></td></tr>
    <tr><td>CMeEE</td><td><a href="https://tianchi.aliyun.com/dataset/dataDetail?dataId=95414">CBLUE</a></td></tr>
<tr><td rowspan="4">Traning Trick</td></tr>
    <tr><td>Gradient Accumulation</td><td></td></tr>
    <tr><td>Learning Rate Warmup</td><td></td></tr>
    <tr><td>Label Smooth</td><td></td></tr>
<tr><td rowspan="3">Misc</td></tr>
    <tr><td>Tokenizer from datasets</td><td></td></tr>
    <tr><td>NER Metrics</td><td><a href="https://github.com/chakki-works/seqeval">seqeval: A Python framework for sequence labeling evaluation</a></td></tr>
</tbody>
</table>

You can easily add your own models and datasets into this framework.

<p id="1"> </p>

# Requirements:

Linux(Tested)/Windows(Not Tested) with Nvidia GPUs.

<p id="2"> </p>

# Install Dependencies.

Recommend to use conda creating a python environment(python==3.9). For example:

```
conda create -n NER python=3.9
```

And run the bash script. If you are using windows, change its extname to .bat.

```
./install_dependencies.sh
```

<p id="3"> </p>

# How To Prepare Datasets

For some reason(copyright and some other things), I can't directly provide datasets to you. You should get the access to these datasets by yourself and put them in specified format into 'assert/raw_datasets' folder, see [here](assets/README.md).

<p id="4"> </p>

# Experiments

<p id="4_1"> </p>

## Hyper Parameters 

<table>
<thead>
<tr><td> </td>
    <td>Optimizer</td>
    <td>Learning Rate</td> 
    <td>Weight Decay</td> 
    <td>Warmup Ratio</td> 
    <td>Label Smoothing</td> 
    <td>Batch Size</td> 
    <td>Gradient Accumulation</td> 
    <td>Total Epoches</td>
    <td>Random Seed</td>
    </tr>
</thead>
<tbody>
<tr><td>BiLSTM-Linear</td>
        <td rowspan="7">Adam</td>
        <td rowspan="2"> 0.001 </td>
        <td rowspan="7"> 5e-3 </td>
        <td rowspan="7"> None </td>
        <td rowspan="7"> None </td>
        <td rowspan="7"> 1 </td>
        <td rowspan="7"> 32 </td>
        <td rowspan="7"> 12 </td>
        <td rowspan="7"> 233 </td></tr>
    <tr><td>BiLSTM-Linear-CRF</td></tr>
    <tr><td>BERT-Linear</td>
        <td rowspan="5">0.0001</td>
        </tr>
    <tr><td>BERT-Linear-CRF</td></tr>
    <tr><td>BERT-BiLSTM-Linear</td></tr>
    <tr><td>BERT-BiLSTM-Linear-CRF</td></tr>
    <tr><td>BERT(Prompt)</td></tr>
</tbody>
</table>

<p id="4_2"> </p>

## Model Parameters

<table>
<thead>
<tr><td>BERT Model</td> <td>Embedding Size(For models without BERT)</td> <td> LSTM Hidden Size </td> <td> LSTM Layers </td> </tr>
</thead>
<tbody>
<tr><td> bert-base </td> <td> 256 </td> <td> 256 </td> <td> 2 </td></tr>
</tbody>
</table>

<p id="4_3"> </p>

## Results

<table>
<thead>
<tr>
    <td> Dataset </td>
    <td> Model </td>
    <td> Overall Span-Based Micro F1 </td>
</tr>
</thead>
<tbody>
<tr><td rowspan="7">CoNLL2003</td><td>BiLSTM-Linear</td>
    <td>0.6517005491858561</td></tr>
<tr><td>BiLSTM-Linear-CRF</td>
    <td>0.6949365863103882</td></tr>
<tr><td>BERT-Linear</td>
    <td>0.8983771483322356</td></tr>
<tr><td>BERT-Linear-CRF</td>
    <td>0.8977943835121128</td></tr>
<tr><td>BERT-BiLSTM-Linear</td>
    <td>0.8819152766110644</td></tr>
<tr><td>BERT-BiLSTM-Linear-CRF</td>
    <td>0.8873846891098599</td></tr>
<tr><td>BERT(Prompt)</td>
    <td></td></tr>

<tr><td rowspan="7">OntoNotes5(Chinese)</td><td>BiLSTM-Linear</td>
    <td></td></tr>
<tr><td>BiLSTM-Linear-CRF</td>
    <td></td></tr>
<tr><td>BERT-Linear</td>
    <td></td></tr>
<tr><td>BERT-Linear-CRF</td>
    <td></td></tr>
<tr><td>BERT-BiLSTM-Linear</td>
    <td></td></tr>
<tr><td>BERT-BiLSTM-Linear-CRF</td>
    <td></td></tr>
<tr><td>BERT(Prompt)</td>
    <td></td></tr>
</tbody>
</thead>
</table>

CMeEE is evaluated by official judger: [https://tianchi.aliyun.com/dataset/dataDetail?dataId=95414](https://tianchi.aliyun.com/dataset/dataDetail?dataId=95414)

<table>
<thread>
<tr><td>Dataset</td><td>Model</td><td> F1 </td></tr>
</thread>
<tbody>
<tr><td rowspan="7">CMeEE</td><td>BiLSTM-Linear</td>
    <td></td></tr>
<tr><td>BiLSTM-Linear-CRF</td>
    <td></td></tr>
<tr><td>BERT-Linear</td>
    <td></td></tr>
<tr><td>BERT-Linear-CRF</td>
    <td></td></tr>
<tr><td>BERT-BiLSTM-Linear</td>
    <td></td></tr>
<tr><td>BERT-BiLSTM-Linear-CRF</td>
    <td></td></tr>
<tr><td>BERT(Prompt)</td>
    <td></td></tr>
</tbody>
</table>

<p id="5"> </p>

# Acknowledgement And Citations
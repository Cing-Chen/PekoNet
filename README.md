# PekoNet

This repository is the source code of [通過生成式文本摘要改進口語法律案件預測效能之研究](https://drive.google.com/file/d/15gQRn6R_midDiPAhmFr7OvOOJIiKvE6s/view?usp=sharing).

- [PekoNet](#pekonet)
  - [Introduction](#introduction)
  - [Environment and Requirements](#environment-and-requirements)
  - [Pretrain Language Models, Data and Checkpoints](#pretrain-language-models-data-and-checkpoints)
    - [Pretrained Language Models](#pretrained-language-models)
    - [Data](#data)
      - [Processed Data (Recommend)](#processed-data-recommend)
      - [Source Data](#source-data)
    - [Checkpoints](#checkpoints)
  - [Usage](#usage)
    - [main.py](#mainpy)
    - [summarize.py](#summarizepy)
    - [generate.py](#generatepy)
    - [convert.py](#convertpy)
    - [analyze.py](#analyzepy)
  - [Contact](#contact)
  - [Citation](#citation)

## Introduction
PEople-Kindly Oriented legal judgment prediction NETwork (PekoNet) is a legal judgment prediction architecture based on abstractive text summarization. The goal of this architecture is to improve the performance of legal judgment prediction on vernacular case facts and the experience of ordinary people who use legal judgment prediction services.

This architecture is composed of two sub-models: Abstractive Text Summarization Model (ATSM) and Legal Judgment Prediction Model (LJPM). We first used a news summary dataset (CNewSum) to train ATSM. Then, we used ATSM to convert Taiwan criminal case facts to vernacular case facts. Last, we used vernacular case facts as the dataset to train LJPM.

In experiments, we prepared two datasets (30K Testing Set, 235 Testing Set) to compare the performance of the models (Orig. Model, Lead-3 Model, PekoNet) on the two prediction tasks (crime, article).

There are the details of datasets and models:
- datasets
  - 30K Testing Set: A dataset there are 300,000 data in
    - `30K Testing Set` (Orig. Fact): Taiwan criminal case facts
    - `30K Testing Set (Summary)`: Taiwan criminal vernacular case facts generated by ATSM
  - 235 Testing Set: A dataset there are 235 data in
    - `235 Orig. Fact`: Taiwan criminal case facts
    - `235 Human Summary`: Taiwan criminal vernacular case facts written by human
- models
  - `Orig. Model`: The model trained by Taiwan criminal case facts
  - `Lead-3 Model`: The model trained by Taiwan criminal vernacular case facts generated by Lead-3 method
  - `PekoNet`: The model trained by Taiwan criminal vernacular case facts generated by ATSM

Pic. 1. and 2. are the results of the experiments. We can see that PekoNet can improve the performance of prediction tasks (especially article prediction task) and has greater generality compared to other models.

![Micro_Results](https://drive.google.com/uc?export=view&id=1e9wPXn53oAAvUBeCmFDQn_hU_C9PSAUR)
> Pic. 1. Micro results

![Macro_Results](https://drive.google.com/uc?export=view&id=1eAljBGa89bn2NIJVFyy2l2r7iI6brobA)
> Pic. 2. Macro results

## Environment and Requirements
- Ubuntu 18.04.6 LTS
- Python 3.7.8
- numpy 1.21.6
- OpenCC 1.1.4
- pytorch-pretrained-bert 0.6.2
- scikit-learn 1.0.2
- tabulate 0.8.10
- torch 1.12.1
- tqdm 4.64.0
- transformers 4.21.2

## Pretrain Language Models, Data and Checkpoints
The architecture of files may be:
```
root
| - models
| - results
|   | - tvt_dataset
|   | - checkpoints
|   ...
| - data
...
```

### Pretrained Language Models
You should download and put `models` folder in the root directory of this repository.
- [models](https://drive.google.com/drive/folders/1ggGjpeRzIX1C9DD6tlXMOa8mVsXE0bm0?usp=sharing)

### Data
#### Processed Data (Recommend)
These are the data we processed and used to train model, do experiments.
You should create `results` folder in the root directory of this repository.
Then, download and put `tvt_dataset` folder in `results`.
- [tvt_dataset](https://drive.google.com/drive/folders/1hV92X5tMccz6a0NJ6N2peO9qfqet26FF?usp=sharing)

#### Source Data
These are the source data we used in this project.
If you want to generate all data by yourself, you should download and put `data` folder in the root of this repository, and use `generate.py` to process data.
- [data](https://drive.google.com/drive/folders/1nbnLc7quxdrfSzPvdvlCSeODhfXmCPVo?usp=sharing)

### Checkpoints
You should create `results` folder in the root directory of this repository.
Then, download and put `checkpoints` folder in `results`.
- [checkpoints](https://drive.google.com/drive/folders/1eXgvMy0WDaTcy0QtuSTMDssp4RqdeQMv?usp=sharing)

## Usage
### main.py
> This file is used to train, evaluate and test LJPM.

Basic Usage:
```
python ./main.py -c CONFIG -m MODE -g GPU [-cp CHECKPOINT_PATH] [-bs BATCH_SIZE] [-dt]
```
> You can use `python ./main.py -h` command to see more information.

Example Usage:
```
python ./main.py -c ./configs/main/bart/one_label/config.ini -m train -g 0 -bs 6 -dt
```

### summarize.py
> This file is used to train, test ATSM.

Basic Usage:
```
python ./summarize.py -c CONFIG -m MODE -g GPU [-cp CHECKPOINT_PATH] [-bs BATCH_SIZE]
```
> You can use `python ./summarize.py -h` command to see more information.

Example Usage:
```
python ./summarize.py -c ./configs/summarize/CNewSum_v2/config.ini -m train -g 0 -bs 6
```

### generate.py
> This file is used to generate data (does not contain human labeling data).

Basic Usage:
```
python ./generate.py -c CONFIG [-g GPU] [-cp CHECKPOINT_PATH]
```
> You can use `python ./generate.py -h` command to see more information.

Example Usage:
```
python ./generate.py -c ./configs/generate/legal_judgment_prediction/lead_3/one_label/config.ini
```

### convert.py
> This file is used to convert text from one Chinese type to another Chinese type by OpenCC.

Basic Usage:
```
python ./convert.py -sdp SOURCE_DIRECTORY_PATH -ddp DESTINATION_DIRECTORY_PATH -c CONFIG
```
> You can use `python ./convert.py -h` command to see more information.
> The config of this file is the OpenCC config, check the config types of OpenCC to know how to use it.

Example Usage:
```
python ./convert.py -sdp ./origin -ddp ./converted -c s2t.json
```

### analyze.py
> This file is used to analyze and get the information of data.

Basic Usage:
```
python ./analyze.py -c CONFIG
```
> You can use `python ./analyze.py -h` command to see more information.

Example Usage:
```
python ./analyze.py -c ./configs/analyze/taiwan_indictments/one_label/config.ini
```

## Contact
If you have any problems, raise an issue or contact [yuxiang.hong.tw@gmail.com](mailto:yuxiang.hong.tw@gmail.com).

## Citation
```
@conference{hong2022pekonet,
    author={洪裕翔、簡國峻、張嘉惠},
    title={通過生成式文本摘要改進口語法律案件預測效能之研究}, 
    booktitle={第二十七屆人工智慧技術與應用國際會議}
    year={2022}
    organization={中華民國人工智慧學會}
}
```

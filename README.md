# Sentiment Analysis for movie review tweets with python
First of all, you need Git LFS in order to clone this repo. More info: https://developer.lsst.io/git/git-lfs.html

## Requirements
* Python (^3.5.3)

## Training model
```shell
cd ml_source/
python train.py <dataset_dir> # <- example: /home/user/aclImdb
```

## Running ml service
```shell
cd ml_source/
python main.py
```

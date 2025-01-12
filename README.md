# DamageDoctor

## Set-Up
Note: Set-up was done with `python 3.12.7` version
General instructions to set up the environment for all experiments
1. Create `venv` (virtual environment) with `python -m venv venv`
2. Activate `venv` with `source venv/bin/activate`
3. Install requirements with `pip install -r requirements.txt`
4. Create a directory named `images/`, all experiments will use this directory to inference on
* Images of your choice can be added here, but [here](https://www.kaggle.com/datasets/pankajkumar2002/random-image-sample-dataset?resource=download) is one neat dataset from kaggle. Download this and move the images into your `images/` dir.

Notes:
* only `.jpg` and `.jpeg` files have been tested to work with it
* deactivate `venv` with `deactivate` command

## Experiments

### `damage_metric_experiment` [VOID]
Ran experiment from [article](https://www.labellerr.com/blog/ml-beginners-guide-to-build-car-damage-detection-ai-model/) in damage_metric_experiment
- Detects damage in car images using MobileNetV2
- Dataset used: [Kaggle Link](https://www.kaggle.com/datasets/anujms/car-damage-detection)

### `img_classification_experiment`
Running regular image classification model locally for offline use. Specs:
- MobileNetV3 implemented with PyTorch
- Using large weight file (`.pth`) trained on [ImageNet](https://paperswithcode.com/dataset/imagenet)
- See `README.md` in directory for additional information to run
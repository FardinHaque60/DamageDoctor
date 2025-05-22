# Car Damage Detection Model

This directory contains a Jupyter notebook implementation of a car damage detection model based on a pre-trained Vision Transformer (ViT) from Hugging Face.

## Damage Classification

The model can classify car damage into six distinct categories:
- **Crack**
- **Scratch**
- **Tire Flat**
- **Dent**
- **Glass Shatter**
- **Lamp Broken**

## Setup and Usage

1. Ensure you have completed the setup steps from the main [README.md](./README.md):
   - Create and activate the virtual environment
   - Install requirements with `pip install -r requirements.txt`
   - Ensure you have the `images/` directory with sample car damage images

2. Additional requirements for this specific notebook:
   ```
   pip install transformers
   ```

3. Run Jupyter Notebook:
   ```
   jupyter notebook
   ```

4. Open the `car_damage_detection.ipynb` file and run the cells.

## Notebook Features

The notebook includes the following functionality:
- Loading a pre-trained car damage detection model from Hugging Face
- Processing and analyzing individual car images
- Batch processing of multiple images
- Visualizing model predictions and confidence scores
- Analyzing dataset statistics to understand model performance
- Two implementation approaches (direct model usage and pipeline-based)

## Model Architecture

The model is based on the beingamit99/car_damage_detection model, which uses a Vision Transformer (ViT bEIT) architecture. This transformer-based approach offers high accuracy for car damage classification tasks.

## Use Cases

This car damage detection model can be applied to various scenarios:
- Auto insurance claim processing
- Vehicle inspection services
- Used car marketplaces
- Automated damage assessment

## Credits

The pre-trained model used in this notebook is from the Hugging Face model repository: [beingamit99/car_damage_detection](https://huggingface.co/beingamit99/car_damage_detection) 
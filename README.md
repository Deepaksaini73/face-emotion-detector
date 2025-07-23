# Facial Emotion Predictor

A deep learning web application that predicts facial emotions using a CNN model built with TensorFlow and Flask.

## Features

- Real-time emotion prediction from uploaded images
- Supports 7 different emotions: angry, disgust, fear, happy, neutral, sad, surprise
- Interactive web interface with image preview
- Mobile-responsive design
- Shows prediction confidence scores

## Tech Stack

- **Deep Learning**: TensorFlow, Keras
- **Backend**: Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Model**: CNN (Convolutional Neural Network)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Deepaksaini73/face-expression-detect-ml.git
cd face-expression-detect-ml
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to `http://localhost:5000`

## Dataset

The model was trained on facial emotion dataset containing images of 7 different emotions. Dataset structure:
```
dataset/
├── train/
│   ├── angry/
│   ├── disgust/
│   ├── fear/
│   ├── happy/
│   ├── neutral/
│   ├── sad/
│   └── surprise/
└── test/
    ├── angry/
    ├── disgust/
    ├── fear/
    ├── happy/
    ├── neutral/
    ├── sad/
    └── surprise/
```

## Model Architecture

- Input Layer: 128x128x3
- Convolutional layers with ReLU activation
- MaxPooling layers
- Dense layers
- Output: 7 classes (emotions)
- Loss: Sparse Categorical Crossentropy
- Optimizer: Adam

## Usage

1. Open the web application
2. Click "Choose Image" to select a face image
3. Preview the selected image
4. Click "Predict Emotion" to get the result
5. View the predicted emotion and confidence score

## Contributing

Feel free to open issues and pull requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Your Name]

## Acknowledgments

- Dataset source [if applicable]
- Any other credits or inspirations

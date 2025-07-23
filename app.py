from flask import Flask, request, render_template, url_for
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load the trained model
model = load_model('model.h5')
class_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def predict_emotion(image_path):
    test_image = image.load_img(image_path, target_size=(128, 128))
    test_image = image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    
    result = model.predict(test_image)
    predicted_index = np.argmax(result)
    predicted = class_labels[predicted_index]
    confidence = float(result[0][predicted_index])
    return predicted, confidence

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    prediction = None
    confidence = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded'
        file = request.files['file']
        if file.filename == '':
            return 'No file selected'
        if file:
            # Save the uploaded file temporarily
            upload_path = os.path.join('uploads', file.filename)
            os.makedirs('uploads', exist_ok=True)
            file.save(upload_path)
            
            # Make prediction
            prediction, confidence = predict_emotion(upload_path)
            
            # Clean up
            os.remove(upload_path)
    
    return render_template('index.html', prediction=prediction, confidence=confidence)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

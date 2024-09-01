import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Load your pre-trained model
model = tf.keras.models.load_model('path/to/your/model')

def generate_caption(image_path):
    # Preprocess the image
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Generate the caption
    predictions = model.predict(img_array)
    caption = decode_predictions(predictions)  # Adjust this to your model's output
    
    return caption

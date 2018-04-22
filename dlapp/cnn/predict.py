import os
import tensorflow as tf
from keras.models import Sequential, load_model
import keras, sys
import numpy as np
from PIL import Image

model = load_model('animal_cnn_aug.h5')
model._make_predict_function()
graph = tf.get_default_graph()

classes = ["サル", "イノシシ", "カラス"]
image_size = 50

def predict_file(file):
    image = Image.open(file)
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    X = []
    X.append(data)
    X = np.array(X)

    global graph
    with graph.as_default():
        result = model.predict([X])[0]
    predicted = result.argmax()
    return classes[predicted]

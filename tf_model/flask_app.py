import json
import os
import tensorflow as tf
import numpy as np
from flask import Flask,jsonify,request
from flask_cors import CORS
from predictor import my_image_predictor
from PIL import Image

app = Flask(__name__)
CORS(app)
@app.route("/predict/",methods=['POST'])
def return_prediction():
  file = request.files['image']
  img = Image.open(file.stream)
  newsize = (224, 224)
  resizedImage = img.resize(newsize)
  img_array = tf.keras.utils.img_to_array(resizedImage)
  img_array = tf.expand_dims(img_array, 0)

  class_names = ['infected', 'notinfected']
  image_predictor = my_image_predictor()
  predictions = image_predictor.predict(img_array)
  score = tf.nn.softmax(predictions[0])
  calculated_prediction = class_names[np.argmax(score)]
  calculated_score = 100 * np.max(score)

  image_dict = {'msg': 'success', 'prediction': calculated_prediction, 'score': calculated_score}
#   app.logger.info('testing info log')
#   app.logger.info(calculated_prediction)
  return jsonify(image_dict)

@app.route("/",methods=['GET'])
def default():
  return "<h1> Welcome to PCOS detection app <h1>"

if __name__ == "__main__":
    app.run() 
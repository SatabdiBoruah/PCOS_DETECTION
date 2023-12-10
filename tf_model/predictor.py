# import pickle
import pandas as pd
import numpy as np
import keras

class my_image_predictor():
  def __init__(self):
    pass
  
  def deserialize(self):
    reconstructed_model = keras.models.load_model("trained_model.h5")
    return reconstructed_model
  
  def predict(self, img_array):
    model = self.deserialize()
    return model.predict(img_array)
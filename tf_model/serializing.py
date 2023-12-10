import pickle
import pandas as pd
import numpy as np
import keras 

model = keras.models.load_model("trained_model.h5")
model.summary()

# Serialize model object into a file called trained_model.pkl on disk using pickle
with open('trained_model.pkl', 'wb') as handle:
    pickle.dump(model, handle, pickle.HIGHEST_PROTOCOL)
# pickle.HIGHEST_PROTOCOL using the highest available protocol 
# (we used wb to open file as binary and use a higher pickling protocol)
import pickle
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import traceback
from joblib import load

# Skin Cancer Model loading
skinCancerModel = load_model('static/models/skinCancer.h5')


# Virus C model loading
with open('static/models/gb_model.pkl', 'rb') as file:
    VirusCModel = pickle.load(file) 

# Lung cancer prediction
lungPrediction = load("static/models/svm_model.joblib")
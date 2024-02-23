import pickle
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import traceback

# Skin Cancer Model loading
skinCancerModel = load_model('static/models/skinCancer.h5')
# Virus C model loading
with open('static/models/VirusC.pkl', 'rb') as file:
    VirusCModel = pickle.load(file) 
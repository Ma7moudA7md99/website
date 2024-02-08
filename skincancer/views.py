from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np


# Create your views here.
# def skinCancer(request):

#     try:
#         model = load_model('static/models/skinCancer.h5')
#         if request.method == "POST":
#             image = request.POST['skinImage']
#             img = cv2.imread(image)
#             resize = tf.image.resize(img, (256, 256))
#             model_result = model.predict(np.expand_dims(resize / 255, 0))
#             result = model_result_text(model_result)
#             print("result")
#             return render(request, 'skin cancer/skin cancer.html', result)
#         else:
#             return HttpResponse('something went wrong')
#     except Exception as e:
#         print(e)
#         # return render(request, 'skin cancer/skin cancer.html')

#     return render(request, 'skin cancer/skin cancer.html')


# def model_result_text(model_result):
#     if model_result < 0.4:
#         result = 'Thank your god you are in good health'
#     elif 0.5 > model_result > 0.4:
#         result = 'Thank your god you are in good health \n but It is best to consult your doctor to ensure your health'
#     else:
#         result = 'you must consult your doctor'

#     return result

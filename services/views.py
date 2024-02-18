from django.shortcuts import render 
from django.http import JsonResponse
from .models import SkinCancer
from dashboard.models import Doctors

import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import traceback
import google.generativeai as genai
genai.configure(api_key="AIzaSyBwuDRRpK-EUa3ERM5TWfreLE3MLyEX0t0")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

medical_mode = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Diabetes mellitus"]
  },
  {
    "role": "model",
    "parts": ["Diabetes mellitus is a chronic metabolic disorder characterized by high blood sugar levels (hyperglycemia) resulting from defects in insulin secretion, insulin action, or both. It can lead to various complications affecting multiple organ systems if not properly managed."]
  },
  {
    "role": "user",
    "parts": ["Osteoporosis"]
  },
  {
    "role": "model",
    "parts": ["Osteoporosis is a condition characterized by weakened bones, making them fragile and more prone to fractures. It occurs when the creation of new bone doesn't keep up with the removal of old bone."]
  },
  {
    "role": "user",
    "parts": ["Anemia"]
  },
  {
    "role": "model",
    "parts": ["Anemia is a medical condition characterized by a deficiency of red blood cells or hemoglobin in the blood. This can result in symptoms such as fatigue, weakness, and shortness of breath due to decreased oxygen-carrying capacity of the blood."]
  },
  {
    "role": "user",
    "parts": ["Arthritis"]
  },
  {
    "role": "model",
    "parts": ["Arthritis is a broad term referring to inflammation of one or more joints, resulting in pain, swelling, stiffness, and decreased range of motion. There are many types of arthritis, including osteoarthritis, rheumatoid arthritis, and gout."]
  },
  {
    "role": "user",
    "parts": ["Pneumonia"]
  },
  {
    "role": "model",
    "parts": ["Pneumonia is an infection that inflames the air sacs in one or both lungs, causing them to fill with fluid or pus. It can range in severity from mild to life-threatening and is typically caused by bacteria, viruses, or fungi."]
  },
  {
    "role": "user",
    "parts": ["Myocardial infarction"]
  },
  {
    "role": "model",
    "parts": ["Myocardial infarction, commonly known as a heart attack, occurs when blood flow to a part of the heart is blocked for a long enough time that part of the heart muscle is damaged or dies. It often presents with symptoms such as chest pain, shortness of breath, and sweating."]
  },
  {
    "role": "user",
    "parts": ["Cataract"]
  },
  {
    "role": "model",
    "parts": ["A cataract is a clouding of the lens in the eye that affects vision. It can cause blurry vision, glare from lights, and difficulty seeing at night. Cataracts are typically age-related but can also develop due to injury, certain medications, or medical conditions like diabetes."]
  },
  {
    "role": "user",
    "parts": ["Gastroesophageal reflux disease (GERD)"]
  },
  {
    "role": "model",
    "parts": [": GERD is a chronic condition where stomach acid flows back into the esophagus, causing irritation and inflammation. Symptoms may include heartburn, regurgitation, chest pain, and difficulty swallowing. Long-term GERD can lead to complications such as esophageal damage and Barrett's esophagus."]
  },
  {
    "role": "user",
    "parts": ["Meningitis"]
  },
  {
    "role": "model",
    "parts": ["Meningitis is an inflammation of the protective membranes covering the brain and spinal cord (meninges). It can be caused by infection with bacteria, viruses, fungi, or other pathogens and presents with symptoms such as headache, fever, stiff neck, and sensitivity to light. Meningitis can be a life-threatening condition and requires prompt medical treatment."]
  },
  {
    "role": "user",
    "parts": ["what is Hypertension"]
  },
  {
    "role": "model",
    "parts": ["Hypertension, also known as high blood pressure, is a condition in which the blood pressure in the arteries is persistently elevated. Blood pressure is determined by the force of blood against the artery walls and the resistance to blood flow in the arteries. Hypertension can lead to severe health complications, including heart attack, stroke, kidney failure, and vision loss."]
  },
])


# Create your views here.
def skinCancer(request):
  model = load_model('static/models/skinCancer.h5')
  if request.method == 'POST':
    try:
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      age = request.POST['age']
      image = request.FILES['skin_image']
      current_instance = SkinCancer.objects.create(first_name=first_name, last_name=last_name, age=age, image=image)
      current_instance.save()
      print(current_instance.image.path)
      img = cv2.imread(str(current_instance.image.path))
      resize = tf.image.resize(img, (256, 256))
      model_result = model.predict(np.expand_dims(resize / 255, 0))
      result = {'result': model_result_text(model_result)}
      return JsonResponse(result)
    except Exception as e:
      print(e)
      return render(request, template_name='skin cancer/skin cancer.html')

  return render(request, 'skin cancer/skin cancer.html')


def medicalTerm(request):
  if request.method == 'POST':
      term = request.POST['question-input']
      question  = term
      medical_mode.send_message(question)
      answer = medical_mode.last.text
      return render(request, 'terminology/terminology.html', {'question': question, 'answer':answer})


  return render(request, template_name='terminology/terminology.html')


def model_result_text(model_result):
  
    percentage = model_result[0] * 100
    if model_result[0] < 0.4:
      result = f'Your result is {percentage[0]:.2f}% \n  It seems that you don\'t have Skin Cancer.'
    elif 0.4 <= model_result[0] < 0.7:
      result  = f"Your result is {percentage[0]:.2f}% \n The lesion may be benign but it could also be malignant."
    else:
      result = f"Your result is {percentage[0]:.2f}%\n Based on the results, there might be a possibility of having Skin Cancer.\n Please consult a doctor immediately!"
    return  result

def doctor(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors': doctors})
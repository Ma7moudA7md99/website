from django.shortcuts import render 
from django.http import JsonResponse
from .models import SkinCancer
from .forms import VirusCForm, LungCancerForm
from dashboard.models import Doctors
from .lib_models import *
from .ai_bot import medical_model


# Create your views here.
def skinCancer(request):
  if request.method == 'POST':
    try:
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      age = request.POST['age']
      image = request.FILES['skin_image']
      current_instance = SkinCancer.objects.create(first_name=first_name,
                                                    last_name=last_name,
                                                    age=age, image=image)
      current_instance.save()
      print(current_instance.image.path)
      img = cv2.imread(str(current_instance.image.path))
      resize = tf.image.resize(img, (256, 256))
      model_result = skinCancerModel.predict(np.expand_dims(resize / 255, 0))
      result =  model_result_text(model_result)
      return JsonResponse({'result' : result})
    except Exception as e:
      print(e)
      return render(request, template_name='skin cancer/skin cancer.html')

  return render(request, 'skin cancer/skin cancer.html')


def medicalTerm(request):
  if request.method == 'POST':
      term = request.POST['question-input']
      question  = term
      medical_model.send_message(question)
      answer = medical_model.last.text


      print(question, answer)
      return JsonResponse({'result' : answer})


  return render(request, template_name='terminology/terminology.html')


def model_result_text(model_result):
  
    percentage = model_result[0] * 100
    if model_result[0] < 0.4:
      result = f'Your result is {percentage[0]:.2f}% <br />  It seems that you don\'t have Skin Cancer.'
    elif 0.4 <= model_result[0] < 0.7:
      result  = f"Your result is {percentage[0]:.2f}% <br /> The lesion may be benign but it could also be malignant."
    else:
      result = f"Your result is {percentage[0]:.2f}% <br /> Based on the results, there might be a possibility of having Skin Cancer. <br /> Please consult a doctor immediately!"
    return  result

# Render Virus C form and load model with results
def virus_c(request):
  if request.method == 'POST':
    form = VirusCForm(request.POST)
    if form.is_valid:
      age = form.data['age']
      gender = form.data['gender']
      alb = form.data['alb']
      alp = form.data['alp']
      alt = form.data['alt']
      ast = form.data['ast']
      bil = form.data['bil']
      che = form.data['che']
      chol = form.data['chol']
      crea = form.data['crea']
      ggt = form.data['ggt']
      prot = form.data['prot']
      values = np.array([age, gender, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot])
      values_reshaped = values.reshape(1, -1)
      model_result = VirusCModel.predict(values_reshaped)
      if  int(model_result[0])==0:
        result = 'You may be infected with the virus but you need to consult your doctor to know the final result'
      else:
        result = "Thank your God you are not infected with the virus"
      form.save()
      return JsonResponse({"result": result})
  else:
    form = VirusCForm()
  return render(request, 'virus c/virus_c.html', {'form': form})

def lung_cancer(request):
  if request.method == "POST":
    form = LungCancerForm(request.POST)
    if form.is_valid():
            # If the form is valid, retrieve the cleaned data
            cleaned_data = form.cleaned_data
            # Now you can access each field's value from cleaned_data dictionary
            smoking = cleaned_data.get('SMOKING')
            yellow_fingers = cleaned_data.get('YELLOW_FINGERS')
            anxiety = cleaned_data.get('ANXIETY')
            peer_pressure = cleaned_data.get('PEER_PRESSURE')
            chronic_disease = cleaned_data.get('CHRONIC_DISEASE')
            fatigue = cleaned_data.get('FATIGUE')
            allergy = cleaned_data.get('ALLERGY')
            wheezing = cleaned_data.get('WHEEZING')
            alcohol_consuming = cleaned_data.get('ALCOHOL_CONSUMING')
            coughing = cleaned_data.get('COUGHING')
            shortness_of_breath = cleaned_data.get('SHORTNESS_OF_BREATH')
            swallowing_difficulty = cleaned_data.get('SWALLOWING_DIFFICULTY')
            chest_pain = cleaned_data.get('CHEST_PAIN')
            gender = cleaned_data.get('gender')
            age = cleaned_data.get('age')
            # from sklearn.model_selection import RandomizedSearchCV
            # from sklearn.svm import SVC
            # param_grid={'C':[0.001,0.01,0.1,1,10,100], 'gamma':[0.001,0.01,0.1,1,10,100]}
            # rcv=RandomizedSearchCV(SVC(),param_grid,cv=5)
            model_array = np.array([smoking, yellow_fingers, anxiety, peer_pressure,
                      chronic_disease, fatigue, allergy, wheezing,
                      alcohol_consuming, coughing, shortness_of_breath,
                      swallowing_difficulty, chest_pain, gender, age]).reshape(1, -1)
            answer = lungPrediction.predict(model_array)
            # answer = rcv.predict(model_array.reshape(-1, 1))
            result = "good" if  answer == 0 else "bad"
            form.save()
            return JsonResponse({'result' : result})
  form = LungCancerForm()
  return render(request, 'lung cancer/lung_cancer.html', {'form':form})
# Retrieve doctor according to specialization 
def doctor(request, specialization):
    doctors = Doctors.objects.filter(specialization=specialization)
    return render(request, 'doctors/doctors.html', {'doctors': doctors})

# Send Messages to doctors
def doctor_message(request, doctor_id):
  doctor = Doctors.objects.get(id=doctor_id)
  return render(request, "doctors/message.html", {"doctor": doctor})
from django.shortcuts import render 
from django.http import JsonResponse
from .models import SkinCancer
from .forms import VirusCForm
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
      print(result)
      return JsonResponse({"result": result})
    print('not valid')
  else:
    form = VirusCForm()
  return render(request, 'virus c/virus_c.html', {'form': form})

def doctor(request, specialization):
    if specialization == "heart":
      doctors = Doctors.objects.filter(specialization="heart")
    elif specialization == "dentist":
      doctors = Doctors.objects.filter(specialization="dentist")
    else:
      doctors = Doctors.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors': doctors})


def doctor_message(request, doctor_id):
  doctor = Doctors.objects.get(id=doctor_id)
  return render(request, "doctors/message.html", {"doctor": doctor})
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def skinCancer(request):
  return render(request, 'skin cancer/skin cancer.html')
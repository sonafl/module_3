from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Успешно, мы молодцы!')
    
# Create your views here.

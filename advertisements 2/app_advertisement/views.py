from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Успешно, мы молодцы!')
    return render(request, 'index.html')
    
# Create your views here.
def top_sellers(request):
    return render(request, 'top-sellers.html')
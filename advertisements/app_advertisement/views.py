from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisement/index.html', context)
    
# Create your views here.
def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

@login_required(login_url = reverse_lazy('adv_post'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisement/advertisement-post.html', context)
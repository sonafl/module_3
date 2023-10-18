from django.urls import path
from .views import index, top_sellers, advertisement_post

urlpatterns = [
    path('', index, name = 'main_page'), 
    path('top_sellers/', top_sellers, name = 'top_sellers'), 
    path('adv_post/', advertisement_post, name = 'adv_post')
]
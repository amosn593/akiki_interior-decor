from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_us', views.contact, name='contact'),
    path('ajax_posting/', views.ajax_posting, name='ajax_posting'),
    path('our_services', views.services, name='services'),
    path('gallery', views.gallery, name='gallery'),
    
]
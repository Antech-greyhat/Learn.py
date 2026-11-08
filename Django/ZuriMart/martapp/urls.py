from django.urls import path
from martapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contacts),
    path('services/', views.services),
    path('subscribe/', views.subscribe),
]

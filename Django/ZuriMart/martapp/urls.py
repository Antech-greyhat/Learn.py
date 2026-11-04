
from django.contrib import admin
from django.urls import path
from martapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', views.about),
    path('contact/', views.contacts),
    path('services/', views.services),
    path('subscribe/', views.subscribe)
]

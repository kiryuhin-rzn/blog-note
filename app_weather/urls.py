from django.urls import path
from app_weather import views

urlpatterns = [
    path('', views.index, name='weather'),  #the path for our index view
]
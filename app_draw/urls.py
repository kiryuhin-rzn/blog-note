from django.urls import path
from app_draw.views import DrawView, ReactView


urlpatterns = [
    path('', DrawView.as_view(), name='draw'),
    path('react/', ReactView.as_view(), name='react'),
]

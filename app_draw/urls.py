from django.urls import path
from app_draw.views import DrawView, ReactView, CanvasView, ExampleView, AnimateView, MenuView, MakeupView


urlpatterns = [
    path('', DrawView.as_view(), name='draw'),
    path('react/', ReactView.as_view(), name='react'),
    path('canvas/', CanvasView.as_view(), name='canvas'),
    path('example/', ExampleView.as_view(), name='example'),
    path('animate/', AnimateView.as_view(), name='animate'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('makeup/', MakeupView.as_view(), name='makeup'),
]

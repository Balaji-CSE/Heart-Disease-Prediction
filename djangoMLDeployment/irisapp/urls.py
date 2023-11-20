from django.urls import path
from irisapp import views

urlpatterns = [
     path('', views.predictor, name='prediction_page'),
  
]

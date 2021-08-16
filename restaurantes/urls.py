from django.urls import path, include
from restaurantes import views

app_name = 'restaurantes'

urlpatterns = [
    path('', views.start , name = "start" )
]
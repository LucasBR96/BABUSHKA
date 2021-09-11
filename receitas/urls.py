from django.urls import path, include
from receitas import views
import re

app_name = 'receitas'

urlpatterns = [
    path('', views.start , name = "start" ),
]
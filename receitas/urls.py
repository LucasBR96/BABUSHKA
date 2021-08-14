from django.urls import path, include
from receitas import views

app_name = 'receitas'

urlpatterns = [
    path('', views.start , name = "start" )
]
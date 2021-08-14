from django.shortcuts import render
from paises.models import Pais
# Create your views here.

def listar_paises( ):
    return Pais.objects.all().order_by('nome',)
from django.shortcuts import render
from paises.views import listar_paises

# Create your views here.
def start( request ):
    tag_dict = {}
    tag_dict[ 'filtro' ] = listar_paises()
    return render( request , "receitas/index.html", tag_dict )
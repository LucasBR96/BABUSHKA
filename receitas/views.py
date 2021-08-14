from django.shortcuts import render
from paises.views import listar_paises
from receitas.models import Receita

from collections import namedtuple
from random import shuffle

#------------------------------------------------------------------------------------
# Auxiliares, não são views

def set_cards():
    card_ojt = namedtuple( "card", [ "nome" , "culinaria" , "thumb" , "desc" ] )
    seq = []
    for x in Receita.objects.all().order_by('nome',):

        nome = x.nome
        culinaria = x.culinaria
        thumb = 'imgs/' + x.thumb

        s = 'descpts/' + x.desc
        with open( s , 'r' ) as f:
            desc = f.read()    
        
        item = card_ojt( nome , culinaria , thumb , desc )
        seq.append( item )
    
    return seq

# Create your views here.
def start( request ):

    tag_dict = {}

    #---------------------------------------------------------
    # Para o filtro, tbm usado para view de restaurante
    tag_dict[ 'filtro' ] = listar_paises()

    #---------------------------------------------------------
    # Cards de receitas
    tag_dict[ 'rec' ] = set_cards()

    return render( request , "receitas/index.html", tag_dict )
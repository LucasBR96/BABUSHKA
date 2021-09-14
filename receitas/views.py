from django.http.response import JsonResponse
from django.shortcuts import render
from paises.views import listar_paises
from receitas.models import Receita , ReceitaCard
from paises.models import PaisForm
from collections import namedtuple
from random import shuffle

#------------------------------------------------------------------------------------
# Auxiliares, não são views

def rend_card( request ):

    '''
        Carrega a informação nescessária para gerar os cards de receitas que serão usados
        nas paginas HTML 
    '''

    #------------------------------------------------------------------------------
    # usando namedtuples por ter mais familiaridade do que query objects
    card_ojt = namedtuple( "card", [ "nome" , "culinaria" , "thumb" , "desc" ] )
    seq = []

    for x in ReceitaCard.objects.all():

        #----------------------------------------------------------------------
        # ReceitaCard -> Receita
        nome = x.rect.nome

        #----------------------------------------------------------------------
        # ReceitaCard -> Receita -> Culinaria
        culinaria = x.rect.culinaria.nome
  
        thumb = x.thumb
        
        #----------------------------------------------------------------------
        # A descrição inicial da receita esta em um arquivo txt dentro da pasta
        # descs. Como é apenas um paragrafo, o texto é leve o suficiente para ser 
        # carregado pela namedtuple
        s = 'descpts/' + x.desc
        with open( s , 'r' ) as f:
            desc = f.read()    
        
        item = card_ojt( nome , culinaria , thumb , desc )
        seq.append( item )
    
    form = PaisForm( request.GET )
    print( form )

    if form.is_valid():
        foo = lambda card: card.culinaria == str( form.cleaned_data[ 'nome' ] )
        seq = list( filter( foo , seq ) )

    return JsonResponse( { x.nome : x for x in seq } )

# Create your views here.
def start( request ):

    tag_dict = {}

    #---------------------------------------------------------
    # Para o filtro, tbm usado para view de restaurante
    tag_dict[ 'filtro' ] = listar_paises()

    return render( request , "receitas/index.html", tag_dict )
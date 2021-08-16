from django.shortcuts import render
from restaurantes.models import Restaurante , RestauranteCard
from collections import namedtuple

# Create your views here.
def loadRestauranteCards( ):
    
    restCard = namedtuple( "restCard" , ["nome", "trad", "cidade", "end", "num", "thumb" , "desc" ] )
    seq = []
    for x in RestauranteCard.objects.all():

        s = 'descpts/' + x.desc
        with open( s , 'r' ) as f:
            desc = f.read()
        thumb = x.thumb

        y = x.rest
        nome = y.nome
        trad = y.tradicao.nome 

        cidade = y.cidade.nome
        end    = y.endereco
        num    = y.numero

        ittem = restCard( nome , trad , cidade , end , num , thumb , desc )
        seq.append( ittem )

    return seq

def start( request ):

    tag_dict = dict()
    
    #-----------------------------------------------------------------------
    # Cards de restaurante
    tag_dict[ 'restCard' ] = loadRestauranteCards()

    return render( request , "restaurantes/index.html", tag_dict )
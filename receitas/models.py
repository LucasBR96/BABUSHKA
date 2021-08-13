from django.db import models
from django.db.models.fields import CharField
from paises.models import Pais

# Create your models here.
class Receita( models ):

    '''
    Cada receita terá duas formas: Card e Pagina

    Card será uma vitrine da receita, vai conter uma foto de thumbanail, seguida por uma tag do país e uma descrição da
    receita. Por fim, no rodapé, haverá um botão com link para a pagina da receita

    A página conterá mais fotos em um carrosel no topo, a lista de igredientes no meio e por fim o modo de preparo

    '''

    nome = models.CharField( max_length = 50 , db_index = True, blank = False )
    slug = models.SlugField( max_length = 50 )
    culinaria = models.ForeignKey( Pais , on_delete = models.CASCADE )

    #-------------------------------------------------------------------
    # Esses aqui são para o modo card, todos são caminhos para as pastas
    # com o conteúdo correspondente.
    thumb = CharField( max_length = 100 , blank = False )
    desc  = CharField( max_length = 100 , blank = False )

    #-------------------------------------------------------------------
    # Esses são para o modo Pagina. Funcionam da mesma maneira que o modo
    # card. Aceitam blank por enquanto
    carr = CharField( max_length = 100 , default = '' )
    igrd = CharField( max_length = 100 , default = '' )
    istr = CharField( max_length = 100 , default = '' )
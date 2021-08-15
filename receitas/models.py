from django.db import models
from django.db.models.fields import CharField
from paises.models import Pais

'''
Cada receita terá duas formas: Card e Pagina

Card será uma vitrine da receita, vai conter uma foto de thumbanail, seguida por uma tag do país e uma descrição da
receita. Por fim, no rodapé, haverá um botão com link para a pagina da receita

A página conterá mais fotos em um carrosel no topo, a lista de igredientes no meio e por fim o modo de preparo

'''

# Create your models here.
class Receita( models.Model ):

    nome = models.CharField( max_length = 50 , db_index = True, blank = False )
    slug = models.SlugField( max_length = 50 )
    culinaria = models.ForeignKey( Pais , on_delete = models.CASCADE )

    class Meta:

        db_table = "receita"
        ordering = ('nome',)

class ReceitaCard( models.Model ):

    #-------------------------------------------------------------------
    # Esses aqui são para o modo card, todos são caminhos para as pastas
    # com o conteúdo correspondente.
    rect  = models.ForeignKey( Receita , on_delete = models.CASCADE )
    thumb = CharField( max_length = 100 , default = 'dummy.png' )
    desc  = CharField( max_length = 100 , default = 'lorem.txt' )

    class Meta:
        db_table = "receitaCard"
    
    def __str__( self ):
        return self.rect.nome

class ReceitaPag( models.Model ):

    #-------------------------------------------------------------------
    # Esses são para o modo Pagina. Funcionam da mesma maneira que o modo
    # card. Aceitam blank por enquanto
    rect  = models.ForeignKey( Receita , on_delete = models.CASCADE )
    carr = CharField( max_length = 100 , default = 'carr_dummy.txt' )
    igrd = CharField( max_length = 100 , default = 'igrd_lorem.txt' )
    istr = CharField( max_length = 100 , default = 'istr_lorem.txt' )

    class Meta:
        db_table = "receitaPag"
    
    def __str__( self ):
        return self.rect.nome

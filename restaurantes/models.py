from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from paises.models import Pais

# Create your models here.
class Cidade( models.Model ):

    '''
        Rio, São Paulo, Curitiba.... caso queira fazer um filtro
    '''

    nome = models.CharField( max_length = 100 , unique = True )

    class Meta:
        db_table = 'cidade'
        ordering = ('nome',)
    
    def __str__( self ):
        return self.nome
    

class Restaurante( models.Model ):

    nome     = models.CharField( max_length = 100 , unique = True )
    tradicao = models.ForeignKey( Pais , on_delete = CASCADE )

    #----------------------------------------------------------------
    # Localizacao geografica
    cidade   = models.ForeignKey( Cidade , on_delete = CASCADE )
    endereco = models.CharField( max_length = 100 , blank = False )
    numero   = models.IntegerField( blank = True )

    #-----------------------------------------------------------------
    # Foco do Trab 5
    cnpj     = models.CharField( max_length = 100 , blank = False  )

    class Meta:
        db_table = 'restaurante'
        ordering = ('nome',)
    
    def __str__( self ):
        return self.nome

class RestauranteCard( models.Model ):

    rest  = models.ForeignKey( Restaurante , on_delete = CASCADE)
    thumb = models.CharField( max_length = 100 , blank = False )
    desc  = models.CharField( max_length = 100 , blank = False )

    class Meta:
        db_table = 'restCard'
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from paises.models import Pais
from collections import namedtuple

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

    def get_desc( self ):

        f = open( self.desc )
        desc = f.read()
        f.close()

        return desc

    def to_render( self ):

        rest_card_render = namedtuple( "cardTup" , [ "nome", "cidade", "trad" , "thumb" , "desc"] )

        return rest_card_render(
            nome   = self.rest.nome,
            cidade = self.rest.cidade.nome,
            trad   = self.rest.tradicao.nome,
            thumb = self.thumb,
            desc  = self.get_desc()
        )

class RestaurantePag( models.Model ):

    rest  = models.ForeignKey( Restaurante , on_delete = CASCADE)

    #-------------------------------------------------------------
    # um unico arquivo txt que contém uma lista de endereços 
    # de varias fotos
    fotos = models.CharField( max_length = 100 , blank = False )

    #-------------------------------------------------------------
    # a critica do restaurante
    desc  = models.CharField( max_length = 100 , blank = False )

    #------------------------------------------------------------
    # avaliação dos restaurantes quanto a 4 quesitos. As notas vão
    # de 0 ( muito ruim ) a 5( excelente )
    cmda_nota = models.IntegerField( default = 0 , blank = False ) # comida 
    ambt_nota = models.IntegerField( default = 0 , blank = False ) # ambiente
    atdm_nota = models.IntegerField( default = 0 , blank = False ) # atendimento
    prec_nota = models.IntegerField( default = 0 , blank = False ) # preco

    def get_desc( self ):

        f = open( self.desc )
        desc = f.read()
        f.close()

        return desc
    
    def get_desc( self ):

        f = open( self.fotos )
        fotos = f.read().split( sep = "\n" )
        f.close()

        return enumerate( fotos , start = 1 )

    def to_render( self ):

        rest_pag_render = namedtuple( "pagTup" , [ "nome", "addr", "fotos" , "critica" , "notas"] )

        return rest_pag_render(
            nome    = self.rest.nome,
            addr    = self.rest.compila_addr(),
            fotos   = self.get_fotos(),
            critica = self.get_desc(),
            notas   = {
                "cmda_nota" : self.cmda_nota,
                "ambt_nota" : self.ambt_nota,
                "atdm_nota" : self.atdm_nota,
                "prec_nota" : self.prec_nota
            }
        )
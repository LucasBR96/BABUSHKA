from django.db import models
from django import forms

# Create your models here.
class Pais( models.Model ):

    '''
    Pais cujo nome vai ser referenciado por receitas e restaurantes como chave estrangeira.
    Não precisa ser um estado soberano, como Rússia ou Romênia, mas também uma tradição regional
    interna de um país, como, por exemplo, Tártaro-Volga, uma minoria mulçumana na Rússia.
    '''

    nome = models.CharField( max_length = 30 , db_index = True, unique = True)
    slug = models.SlugField( max_length = 30 )

    class Meta:

        db_table = 'pais'
        ordering = ('nome',)
    
    def __str__(self):
        return self.nome


class PaisForm( forms.Form ):

    class Meta:
        fields = ("nome")
    
    nome = forms.ModelChoiceField(
        empty_label = "--- Selecione ---",
        queryset = Pais.objects.all().order_by( 'nome' ),
        widget = forms.Select( attrs = {"class" : "form-control"} )
    )
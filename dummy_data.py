from paises.models import Pais
from receitas.models import Receita , ReceitaCard

def set_paises():

    Pais.objects.all().delete()

    paises = []
    paises.append( ( "Russia" , "RUS" ) )
    paises.append( ( "Armenia" , "ARM" ) )
    paises.append( ( "Polônia" , "POL" ) )
    paises.append( ( "Hungria" , "HGR" ) )

    for nom , slg in paises:
        p = Pais( nome = nom , slug = slg )
        p.save()

def set_receitas():

    Receita.objects.all().delete()

    comidas = []
    comidas.append( ( "Tan apur" , "Armenia" ) )
    comidas.append( ( "Paprikash" , "Hungria" ) )
    comidas.append( ( "Goulash" , "Hungria" ) )
    comidas.append( ( "Borscht" , "Russia" ) )
    comidas.append( ( "Zurek" , "Polônia" ) )

    for nom , cat in comidas:

        origem = Pais.objects.get( nome = cat )
        slg = nom.lower()
        p = Receita( nome = nom , slug = slg , culinaria = origem , thumb = "dummy.png" , desc = "lorem.txt" )
        p.save()

def set_receitasCards():

    ReceitaCard.objects.all().delete()

    cards = []
    cards.append( ( "Tan apur" , "Tan_apur.jpg" ) )
    cards.append( ( "Paprikash" , "Paprikash.jpeg" ) )
    cards.append( ( "Goulash" , "Goulash.jpg" ) )
    cards.append( ( "Borscht" , "Borscht.jpg" ) )
    cards.append( ( "Zurek" , "Zurek.jpg" ) )

    for nom , thb in cards:

        origem = Receita.objects.get( nome = nom )
        p = ReceitaCard( thumb = thb , rect = origem )
        p.save()


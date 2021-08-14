from paises.models import Pais
from receitas.models import Receita

paises = []
paises.append( ( "Russia" , "RUS" ) )
paises.append( ( "Armenia" , "ARM" ) )
paises.append( ( "Polônia" , "POL" ) )
paises.append( ( "Hungria" , "HGR" ) )

for nom , slg in paises:
    p = Pais( nome = nom , slug = slg )
    p.save()

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


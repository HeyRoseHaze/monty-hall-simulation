from lmd import spr_wybor, wybor_gracza, odrzucenie_gracza
from logic import odrzucenie_skrzyni, losowanie_nagrody, final

wybor = wybor_gracza()
nagroda = losowanie_nagrody()
odrzucenie_skrzyni(nagroda, wybor)
decyzja = odrzucenie_gracza()
final(nagroda, wybor, decyzja)
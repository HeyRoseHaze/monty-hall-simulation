from lmd import wybor_gracza, odrzucenie_gracza
from logic import odrzucenie_skrzyni, losowanie_nagrody, final

liczba_wygranych = 0
liczba_przegranych = 0

while True:
    wybor = wybor_gracza()
    nagroda = losowanie_nagrody()
    odrzucenie_skrzyni(nagroda, wybor)
    decyzja = odrzucenie_gracza()

    wygrana = final(nagroda, wybor, decyzja)

    if wygrana:
        liczba_wygranych += 1
    else:
        liczba_przegranych += 1  
    print(f"Liczba wygranych: {liczba_wygranych}\nLiczba przegranych: {liczba_przegranych}")




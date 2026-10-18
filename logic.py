import random

def losowanie_nagrody():
    skrzynia_z_nagroda = random.randint(1,3)
    return skrzynia_z_nagroda

def odrzucenie_skrzyni(skrzynia_z_nagroda, wybor_uzytkownika):
    while True:
        odrzucona_skrzynia = random.randint(1,3)
        if odrzucona_skrzynia == skrzynia_z_nagroda:
            continue
        elif odrzucona_skrzynia == wybor_uzytkownika:
            continue
        else: 
            print(f"Odrzucono: {odrzucona_skrzynia}")
            break

def final(skrzynia_z_nagroda, wybor_uzytkownika, decyzja):
    liczba_przegranych = 0
    liczba_wygranych = 0
    if decyzja == "nie":
        if skrzynia_z_nagroda == wybor_uzytkownika:
            print("Wygrałeś")
            return True
        else: 
            print(f"Przegrałeś. Nagroda była w skrzyni {skrzynia_z_nagroda}")
            return False
    if decyzja == "tak":
        if skrzynia_z_nagroda == wybor_uzytkownika:
            print(f"Przegrałeś. Nagroda była w skrzyni {skrzynia_z_nagroda}")
            return False
        else: 
            print("Wygrałeś")
            return True

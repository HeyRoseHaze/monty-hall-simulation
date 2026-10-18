import random



        
def spr_wybor(wybor):
        try:
            wybor_uzytkownika = int(wybor)
            if wybor_uzytkownika > 3 or wybor_uzytkownika < 1:
                print(f"Podałeś {wybor_uzytkownika}. Liczba musi być z zakesu 1-3.\nMusisz podać jeszcze raz")
                return None
            else:
                print(f"Wybrano: {wybor_uzytkownika}")
                return wybor_uzytkownika
        

        except ValueError:
            print("To nie jest liczba. Podaj liczbę z zakresu 1-3!")


def wybor_gracza():
    while True:
        try:
            wybor_uzytkownika = int(input("Wybierz skrzynie (1-3): "))
            
            if wybor_uzytkownika < 1 or wybor_uzytkownika > 3:
                print(f"Podałeś {wybor_uzytkownika}. Liczba musi być z zakresu 1-3.\nMusisz podać jeszcze raz.")
            else:
                print(f"Wybrano {wybor_uzytkownika}")
                return wybor_uzytkownika
                
        except ValueError:
            print("To nie jest liczba. Podaj liczbę z zakresu 1-3!")




# while True:
#     try:
#         wybor_uzytkownika = int(input("Wybierz opcję (1-3): "))
#         break
#     except ValueError:
#         print('To nie jest liczba. Podaj liczbę z zakresu 1-3!')
# wybor_uzytkownika = wybor()
# sprawdz_wybor(wybor_uzytkownika)

# skrzynia_z_nagroda = random.randint(1, 3)

# while True:
#     odrzucona_skrzynia = random.randint(1, 3)
#     if odrzucona_skrzynia == skrzynia_z_nagroda:
#         continue
#     elif odrzucona_skrzynia == wybor_uzytkownika:
#         continue
#     else:
#         print(f"Odrzucono: {odrzucona_skrzynia}")
#         break 

# decyzja = input("Czy zmieniasz skrzynie? ")
# if decyzja == "tak":
#     if skrzynia_z_nagroda == wybor_uzytkownika:
#         print('Przegrałeś')
#     else: print('Wygrałeś')
# if decyzja == "nie":
#     if skrzynia_z_nagroda == wybor_uzytkownika:
#         print('Wygrałeś')
#     else:
#         print('Przegrałeś')
        


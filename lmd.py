import random

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

def odrzucenie_gracza():
    while True:
        decyzja = input("Czy zmieniasz skrzynie? ").strip().lower()
        if decyzja not in ("tak", "nie"):
            print("zla decyzja")
        else:
            return decyzja

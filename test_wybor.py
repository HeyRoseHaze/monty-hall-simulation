from lmd import spr_wybor

def test_wybor():
    """CZY ZADZIALA NA 3"""
    wybor = spr_wybor(3)
    assert wybor == 3



# while True:
#     wybor = input('Podaj liczbę z zakresu 1-3: ')
#     if wybor == 'q':
#         break

#     wybor_uzytkownika = spr_wybor(wybor)
    
"""
zapouzdreni = ochrana udaju pred okolnim svetem, ale vrati SPRAVNY VYSLEDEK
"""

import random

class Karta:
    "class represents Karta"
    def __init__(self, _barva, _hodnota):
        self.barva = _barva
        self.hodnota = _hodnota

    def vypis_kartu(self):
        #print(self.barva, self.hodnota, sep="")
        print(f"{self.barva}{self.hodnota}")

    def vrat_kartu(self):
        """
        Funkce vraci kartu
        :return: slovnik karet
        """
        return [self.barva, self.hodnota]


class Balicek:
    "class represents Balicek"
    def __init__(self):
        self.__karty = []
        barvy = ["♣", "♦", "♥", "♠"]
        hodnoty = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        for barva in barvy:
            for hodnota in hodnoty:
                self.__karty.append(Karta(barva, hodnota))
        self.zamichat()

    def zamichat(self):
        random.shuffle(self.__karty)

    def vypis_balicek(self):
        self.zamichat()
        for karta in self.__karty:
            karta.vypis_kartu()

    def vydej_kartu(self):
        return self.__karty.pop()

class Hrac:
    "class represents Hrac"
    def __init__(self, _jmeno):
        self.jmeno = _jmeno
        self.penize = 1000
        self.__ruka = []

    def vezmi_kartu(self, _karta):
        self.__ruka.append(_karta)

    def vypis_karty(self):
        for karta in self.__ruka:
            karta.vypis_kartu()

class Krupier:
    "class represents Krupier"
    def __init__(self):
        self.__ruka = []

    def lizni(self, _pocet, balicek):
        for i in range(_pocet):
            self.__ruka.append(balicek.vydej_kartu())

    def rozdej(self, pocet, hrac, balicek):
        for i in range(pocet):
            hrac.vezmi_kartu(balicek.vydej_kartu())

    def vypis_karty(self):
        for karta in self.__ruka:
            #print(karta.barva, karta.hodnota, sep="", end=" ")
            print(f"{karta.barva}{karta.hodnota}", end=" ") #druha moznost


b1 = Balicek()
h1 = Hrac("Jakub")
k1 = Krupier()
k1.lizni(2, b1)
k1.rozdej(2, h1, b1)

print("Dealer: ", end=" ")
k1.vypis_karty()

print("Hrac: ", end=" ")
h1.vypis_karty()
'''
Created on 6 janv. 2016

@author: Yimtchen
'''

class Voiture:

    def __init__(self, hauteur, longueur, immatriculation):
        self.__hauteur = hauteur
        self.__longueur = longueur
        self.immatriculation = immatriculation
        self.__estDansParking = False
        self.__estDansEntrepot = False

    @property
    def estDansParking(self): return self.__estDansParking
    @estDansParking.setter
    def estDansParking(self,changement) : self.__estDansParking = changement

    @property
    def estDansEntrepot(self): return self.__estDansEntrepot

    @estDansEntrepot.setter
    def estDansEntrepot(self,changement) : self.__estDansEntrepot = changement



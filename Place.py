'''
Created on 6 janv. 2016

@author: Yimtchen
'''

class Place :
    def __init__(self,num,longueur,hauteur):
        self.__num = num
        self.__longueur = longueur
        self.__hauteur = hauteur
        self.__estLibre = True
        self.__placeAbonne = False


    @property
    def estLibre(self) : return self.__estLibre

    @estLibre.setter
    def estLibre(self,changement) : self.__estLibre = changement

    @property
    def placeAbonne(self): return self.__placeAbonne

    @placeAbonne.setter
    def placeAbonne(self,changement): self.placeAbonne = changement

    #Ajout getteur et setteurs de hauteur...

    @property
    def longueur(self): return self.__longueur

    @longueur.setter
    def longuer(self, value): self.__longueur = value

    @property
    def hauteur(self): return self.__hauteur

    @hauteur.setter
    def hauteur(self): self.__hauteur




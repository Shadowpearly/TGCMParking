'''
Created on 6 janv. 2016

@author: Yimtchen
'''

class Placement:


    def __init__(self, dateDebut, voiture, place):
        self.__dateDebut = dateDebut
        self.__dateFin = 0
        self.__estEnCours = False
        self.__voiture = voiture
        self.__place = place

    @property
    def estEnCours(self): return self.__estEnCours
    @estEnCours.setter
    def estEnCours(self,changement): self.__estEnCours = changement

    @property
    def dateFin(self): return self.__dateFin
    @dateFin.setter
    def dateFin(self,date): self.__dateFin = date


'''
Created on 6 janv. 2016

@author: Yimtchen
'''
from Place import *
from Voiture import *
from Placement import *
from _datetime import date


class Parking:

    def __init__(self,nb_places, nb_etages, prix):
        self.__nb_places = nb_places
        self.__nb_etages = nb_etages
        self.__prix = prix
        #self.__places = self.initPlaces()
        self.__placesLibre = {}
       # self.__placesLibre = self.initPlacesLibres()
        self.__placesOccupee = {}
        self.__parkingVIP = []
        self.__placements = []

    @property
    def listabonner(self): return self.__listabonner
    @listabonner.setter
    def listeabonner(self, id, carte): self.__listeabonner[id] = carte

    def rechercherabo(self, id):
        return self.__listeabonner.get(id, False)

    def initPlaces(self):
        retour = []
        for i in range(0,self.__nb_places):
            if(0 <= i <= self.__nb_places//2):
                temp = Place(i,100,20)
                retour.append(temp)
            elif((self.__nb_places)/2 < i <= self.__nb_places//4*3):
                temp = Place(i,200,40)
                retour.append(temp)
            else:
                temp = Place(i,300,60)
                retour.append(temp)
        return retour

    def initPlacesLibres(self):
        for i in range(0,self.__nb_places):
            temp = self.__places[i]
            longueur = temp.hauteur
            largeur = temp.largeur
            value = longueur+"x"+largeur
            retour[i] = value

    def trouverPlace(self,longueur,largeur):
        value = longueur+"x"+largeur
        try :
            temp = self.__placesLibre(value) #on cherche dans les places libres la place qui correspond à la dim
            print(temp.type()) #à vérifier si dans type il y a une seule valeur ou bien toutes les valeures possibles
        except KeyError as erreur:
            print("Il n'y a pas de place libre de dimensions : "+longueur+"x"+largeur)
            return -1
        self.__placesOccupee[temp] = value# et on l'ajoute aux places occupées
        return temp #on retourne cette place trouvée afin de pouvoir garer la voiture

    def nbPlacesLibre(self):
        return self.__placesLibre.__len__()

    def teleporterVIP(self,voiture):
        place = self.trouverPlace(voiture.longueur, voiture.largeur)
        placement = Placement(date, voiture, place)
        self.__placements.append(placement)
        self.__parkingVIP.append(voiture)

    def teleporterVoiture(self,voiture):
        place = self.trouverPlace(voiture.longueur, voiture.largeur)
        placement = Placement(date, voiture, place)
        self.__placements.append(placement)
        self.__placesLibre.__delattr__(place)#on enlève cette place des places libres
        self.__placesOccupee[place] = voiture.longueur+"x"+voiture.largeur # et on l'ajoute aux places occupées

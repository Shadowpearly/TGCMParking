'''
Created on 6 janv. 2016

@author: Yimtchen
'''

import uuid

class Client:

    def __init__(self, prenom, nom, addr, datenais):
        self.__prenom = prenom
        self.__nom = nom
        self.__addr = addr
        self.__datenais = datenais
        self.__identifiant = str(uuid.uuid1())


    def __str__(self):
        return "Prenom: "+self.__prenom+ "\n Nom:    "+self.__nom+"\n Adresse Postale:  "+self.__addr+"\nIdentifiant: "+\
               self.__identifiant

    @property
    def estAbonne(self): return self.__estAbonne
    @estAbonne.setter
    def estAbonne(self,changement): self.__estAbonne = changement

    @property
    def estSuperAbonne(self): return self.__estSuperAbonne
    @estSuperAbonne.setter
    def estSuperAbonne(self,changement): self.__estSuperAbonne = changement

    @property
    def identifiant(self): return self.__identifiant




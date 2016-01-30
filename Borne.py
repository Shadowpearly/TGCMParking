from Client import *


class Borne:
    def __init__(self,id):
        self.__id = id

    def souscrire_abonnement(self,client):
        if(client.estAbonne):
            return False
        else:
            client.estAbonne = True

    def souscirre_super_abo(self,client):
        if(client.estSuperAbonne):
            return False
        else:
            client.estSuperAbonne = True

    def resilierabonnement(self,client):
        if(client.estAbonne==False):
            return False
        else:
            client.estAbonne = False
            return True

    def resilier_super_abo(self,client):
        if(client.estSuperAbonne == False):
            return False
        else:
            return True



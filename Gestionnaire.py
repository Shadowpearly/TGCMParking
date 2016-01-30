

class Gestionnaire:

    def __init__(self):

        self.__listeabonner = {}
        self.__listeclient = {}

    @property
    def listeabonner(self): return self.__listeabonner

    @listeabonner.setter
    def listeabonner(self, id, carte): self.__listeabonner[id] = carte


    @property
    def listeclient(self): return self.__listeclient

    @listeclient.setter
    def listeclient(sel, idcli, client ): self.__listeclient[idcli] = client


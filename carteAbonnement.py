'''
Created on 14 janv. 2016

@author: yannis
'''

from Client import *

class CarteAbonnement():
    '''
    Un client abonner à une carte d'abonnement
    '''

    def __init__(self, client):
        '''
        Une carte d'abonnement possède un identifiant unique égal à celui du client.
        Si le client est suepr abonner alors il à droit à divers services et au pack garenti
        si non si il est abonner si à uniquement droit aux services.
        '''
        id = client.Identifiant
        self.__Services = False
        self.__Garantie = False

    @property
    def service(self): return self.__Services
    @service.setter
    def service(self, changement): self.__Services = changement

    @property
    def garantie(self): return self.__Garantie
    @garantie.setter
    def garantie(self, chang): self.__Garantie = chang

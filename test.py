'''
Created on 15 janv. 2016

@author: yannis
'''
from Client import *
from Borne import *

if __name__ == '__main__':

    monclient = borne1.enregistrerclient(prenom, nom, adresse, datenaissance)

    resiliation = borne1.resilierabonnement(monclient)
    print("Resiliation avant souscription AB ")
    print(resiliation)
    superresiliation = borne1.resiliersuperabonnement(monclient)

    print("Resiliation avant souscription SAB")
    print(superresiliation)

    print("Souscription à un abonnement:    ")
    souscriptionAbonement = borne1.souscrireabonnement(monclient)
    print(souscriptionAbonement)

    print("Souscription à un superAbonnement : ")
    superAbo = borne1.souscrireauperabonnement(monclient)
    print(superAbo)

    resiliation = borne1.resilierabonnement(monclient)
    print("Resiliation après souscription ")
    print(resiliation)

    superresiliation = borne1.resiliersuperabonnement(monclient)
    print("Resiliation apres souscription")
    print(superresiliation)

'''
Created on 6 janv. 2016

@author: Yimtchen
'''

from Placement import *

from _datetime import date

class Teleporteur :

    def __init__(self,num):
        self.__num = num

    def teleporterVoiture(self,v,p):
        placement = Placement(date, v,p)
        return placement


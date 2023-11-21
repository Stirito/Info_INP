# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:33:05 2023

@author: benoi
"""
from Piles import *

#2.3

def Renverse(P):
    G = Creer_Pile()
    for i in range(len(P)):
        Empiler(G, Depiler(P))
    return G

def Renverse_2(P):
    return P[::-1]




            
        
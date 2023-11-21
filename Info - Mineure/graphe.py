# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:55:09 2023

@author: benoi
"""

from Piles import *
from Files import *
from math import *

M = [[0,"A","B","C","D","E","F","G","H","I"],
     ["A",0,1,1,0,0,0,0,0,0],
     ["B",0,0,0,0,1,0,0,0,0],
     ["C",0,0,0,0,1,0,1,0,0],
     ["D",0,0,1,0,0,0,0,0,0],
     ["E",0,0,0,0,0,1,0,1,0],
     ["F",0,1,0,0,0,0,0,0,0],
     ["G",0,0,0,1,0,0,0,1,1],
     ["H",0,0,0,0,0,0,1,0,0],
     ["I",0,0,0,0,0,0,0,1,0]]

M2 = [[0,"A","B","C","D","E","F"],["A",0,1,1,0,0,0],["B",0,0,0,0,1,0]]

M3 = [[0,"A","B","C","D","E","F","G","H","I"],
     ["A",0,1,1,1,0,0,0,0,0],
     ["B",1,0,1,0,1,1,0,0,0],
     ["C",1,1,0,1,0,1,0,0,0],
     ["D",1,0,1,0,0,1,1,0,0],
     ["E",0,1,0,0,0,1,0,1,0],
     ["F",0,1,1,1,1,0,1,1,1],
     ["G",0,0,0,1,0,1,0,0,1],
     ["H",0,0,0,0,1,1,0,0,1],
     ["I",0,0,0,0,0,1,1,1,0]]
M3_adjacent = [[0,"A","B","C","D","E","F","G","H","I"],
    ["A", 0, 7, 16, 8, inf, inf, inf, inf, inf],
    ["B", 7, 0, 5, inf, 4, 9, inf, inf, inf],
    ["C", 16, 5, 0, 3, inf, 4, inf, inf, inf],
    ["D", 8, inf, 3, 0, inf, 10, 4, inf, inf],
    ["E", inf, 4, inf, inf, 0, 3, inf, 2, inf],
    ["F", inf, 9, 4, 10, 3, 0, 7, 6, 8],
    ["G", inf, inf, inf, 4, inf, 7, 0, inf, 7],
    ["H", inf, inf, inf, inf, 2, 6, inf, 0, 6],
    ["I", inf, inf, inf, inf, inf, 8, 7, 6, 0]]


def Degre(M,S):
    if S in M[0]:
        g = M[0].index(S)
        s = 0
        for el in M[g]:
            if el  == 1:
                s+=1
    return s


def Voisins(M,S):
    L = []
    if S in M[0]:
        g = M[0].index(S)
        T = M[g]
        print(T)
        s = 0
        for el in T:
            if el == 1:
                L.append(M[0][s])
            s+=1
        
    return L

def ParcoursLargeur(M : list,sommet :str):
    Atraiter = [sommet]
    DejaTraite = [sommet]
    while Atraiter != []:
        s = Defiler(Atraiter)
        Traiter(s)
        G = Voisins(M,s)
        for voisin in G:
            if voisin not in DejaTraite:
                Enfiler(Atraiter,voisin)
                Enfiler(DejaTraite,voisin)
        
        print(Atraiter)


def ParcoursProfondeur(M : list,sommet :str):
    Atraiter = [sommet]
    DejaTraite = [sommet]
    while Atraiter != []:
        s = Depiler(Atraiter)
        Traiter(s)
        G = Voisins(M,s)
        for voisin in G:
            if voisin not in DejaTraite:
                Empiler(Atraiter,voisin)
                Empiler(DejaTraite,voisin)
        print(Atraiter)
            
def Traiter(s:str):
    print(s)
#print(ParcoursProfondeur(M,"A"))


def Dijsktra(M:list,s:str):
    Pris = []
    NonPris = []
    return



def Minimum(L:list):
    plus_petit_chemin = min([el[1] for el in L])
    for el in L:
        if el[1] == plus_petit_chemin:
            return el
        
def Appartient(t :str,L:list):
    return t in [el[0] for el in L]

def Modifier(L: list,t:str,d :int):
    G = []
    for el in L:
        if el[0] == t:
            G.append((t,d))  
        else:
            G.append(el)  
    L = G
    return L

def Delta(L:list,t:str):
    return 
print(Modifier([("A",12),("B",14)],"A",1))
from Pilescopy import *


P,Q = [9,4,2,7,6,9], [17,2,3,19,4,6,20]

def Max(P:list):
    L = Creer_Pile()
    
    a =Depiler(P)
    Empiler(L,a)
    b = 0
    
    while P != []:
        
        if b < a:
            
            b = a
        a = Depiler(P)
        Empiler(L,a)
    G = Creer_Pile()
    
    while L != []:
        Empiler(G,Depiler(L))
    return trouve_indice_valeur(G,b)

def trouve_indice_valeur(P,valeur):
    j = 1
    while P != []:
        a = Depiler(P)
        if a == valeur:
            break
        j+=1
    return j


def Somme(P:list):
    L = Creer_Pile()
    somme = 0
    if Pile_Vide(P):
        raise Exception("Pile vide pas de somme")
    else:
        while P != []:
            a = Depiler(P)
            somme+=a
            Empiler(L,a)
        while L != []:
            Empiler(P,Depiler(L))
    return P,somme

def Renverser(P:list,j:int):
    L = Creer_Pile()
    D = Creer_Pile()
    for i in range(j):
        a = Depiler(P)
        Empiler(L,a)
    
  
    while L != []:
        Empiler(D,Depiler(L))
    
    while D != []:
        Empiler(P,Depiler(D))
    return P

print(Renverser(P,3))
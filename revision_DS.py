from Pilescopy import *


P,Q = [9,4,2,17,6,9], [17,2,3,19,4,6,20]

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
  
    return abs(Longueur(L)-trouve_indice_valeur(L,b))+1

def trouve_indice_valeur(P,valeur):
    j = 1
    while P != []:
        a = Depiler(P)
        if a == valeur:
            break
        j+=1
    return j
print(Max(Q),Max(P))


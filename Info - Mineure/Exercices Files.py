# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:09:09 2023

@author: benoi
"""

from Files import *

#2.4

def Permut(F,n):
    j = 0
    while j < n:
        
        Enfiler(F, Defiler(F))
        j+=1
    
#2.5

def Ajouter(Filecinema,individu):
    
    E = Creer_File()
    
    flag = False
    
    for i in range(Longueur(Filecinema)):
        
        a = Defiler(Filecinema)
        
        if a == individu:
            flag = True
        Enfiler(E, a)
        
    t = Premier(E)
    
    if not flag:
        
        Enfiler(E,individu)
        return E
    
    
    else:
        
        while Premier(E) != individu:
          
            Permut(E,1)
            
        Enfiler(Filecinema,individu)
       
        for i in range(Longueur(E)):
           
            Enfiler(Filecinema, Defiler(E))
        
        
        while Premier(Filecinema) != t:
            Permut(Filecinema,1)
        
        return Filecinema

print(Ajouter(["a","b","c","e"], "e"))

def Retirer(Filecinema):
    
    
    tigars = Defiler(Filecinema)
    while tigars == Premier(Filecinema):
        Defiler(Filecinema)
   
       
    return Filecinema


            
                
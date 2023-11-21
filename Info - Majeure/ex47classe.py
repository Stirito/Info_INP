from math import pi
from random import shuffle,randint
class Point:
  def __init__(self,x=0,y=0,z=0):
    self.x = x
    self.y = y
    self.z = z
  def Coordonnees(self):
    return (self.x,self.y,self.z) 
class Cercle:
  def __init__(self,centre,rayon):
    self.centre = centre
    self.rayon = rayon
    
  def Afficher(self):
    print(self.centre.Coordonnees(),self.rayon)
  def Aire(self):
    return pi*(self.rayon**2)

class Cylindre(Cercle):
  def __init__(self, centre, rayon,hauteur):
    super().__init__(centre, rayon)
    self.hauteur = hauteur
  def Volume(self):
    return self.Aire()*self.hauteur
  
class Cone(Cylindre):
  def __init__(self, centre, rayon, hauteur):
    super().__init__(centre, rayon, hauteur)
  def Volume(self):
    return Cylindre.Volume(self)/3


#Ex 4.7

class Carte:
  valeur_correcte = ["Deux","Trois","Quatre","Cinq","Six","Sept","Huit","Neuf","Dix","Valet",
"Dame","Roi","As"]
  couleur_correcte = ["Coeur","Carreau","Trèfle","Pique"]
  def __init__(self,valeur,couleur):
    try:
       assert valeur in Carte.valeur_correcte
       self.valeur = valeur
    except AssertionError:
      print("Mettez nom de carte valide")
      
    try:
       assert couleur in Carte.couleur_correcte
       self.couleur = couleur
    except AssertionError:
      print("Mettez couleur valide")
      
    self.nom_complet = self.valeur + " de " + self.couleur

class JeuDeCartes:
  def __init__(self) :
    self.MainA = []
    self.MainB = []
    self.Table = []
    self.Paquet = [Carte(valeur,couleur) for valeur in Carte.valeur_correcte for couleur in Carte.couleur_correcte]
  def Battre(self):
    for i in range(randint(10,50)):
      shuffle(self.Paquet)
    
  def Retirer(self,Paquet_a_retirer:list):
    
    if Paquet_a_retirer == []:
      raise Exception("Paquet Vide je ne peux retirer")
    
    carte_a_enlever = Paquet_a_retirer[len(Paquet_a_retirer)-1]
    
    Paquet_a_retirer.remove(carte_a_enlever)
    return carte_a_enlever
  
  def Distribuer(self):
    self.Battre()
      
    
    
    is_A = False
    while self.Paquet != []:
      carte = self.Retirer(self.Paquet)
      if is_A == False:
        self.MainA.append(carte)
        is_A = True
      else:
        self.MainB.append(carte)
        is_A = False
     
      self.Battre()
      
 
  def Jouer(self,Main_joueur):
    
    derniere_carte = self.Retirer(Main_joueur)
    self.Table.append(derniere_carte)
    
    return derniere_carte
  
  def GagnerManche(self,Main_Joueur):
    shuffle(self.Table)
    for carte in self.Table:
      Main_Joueur.insert(0,carte)
      self.Retirer(self.Table)
    
    
  def LancerPartie(self):
    
    self.Distribuer()
    
 
    
    while  self.MainA != [] and self.MainB != []:
      
      if self.MainA != [] and self.MainB != []:
          
          carte_A = self.Jouer(self.MainA)
          carte_B = self.Jouer(self.MainB)
      
      
      
      
      valeur_carte_A = Carte.valeur_correcte.index(carte_A.valeur)
      valeur_carte_B = Carte.valeur_correcte.index(carte_B.valeur)
      
      if valeur_carte_A < valeur_carte_B:
   
        self.GagnerManche(self.MainB)
      elif valeur_carte_B < valeur_carte_A:
 
        self.GagnerManche(self.MainA)
      elif valeur_carte_A == valeur_carte_B:
   
        
        if self.MainA != [] and self.MainB != []:
       
          self.Jouer(self.MainA)
          self.Jouer(self.MainB)
        elif self.MainA == [] and self.MainB != []:
          self.GagnerManche(self.MainB)
          
        elif self.MainB == [] and self.MainA != []:
          self.GagnerManche(self.MainA)
          
        
        
        
    if self.MainB == []:
      return "Main A"
    elif self.MainA == []:
      return "Main B"
      
def Prob():
  c,d = 0,0
  for i in range(200):
    A = JeuDeCartes()
    A.LancerPartie()
    if A.LancerPartie() == "Main A":
      c+=1
    else:
      d+=1
  return c,d


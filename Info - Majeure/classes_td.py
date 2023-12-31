from random import randint
    
# ex 4.8  

class Domino:
  def __init__(self,A,B) -> None:
    self.A = A
    self.B = B
  def Afficher(self):
    return (self.A,self.B)
  def Valeur(self):
    return self.A + self.B
  def EstDouble(self):
    return self.A == self.B
  def Retourner(self):
    return Domino(self.B,self.A)

class Joueur:
  def __init__(self,strategie) -> None:
    
    self.main = []
    self.jouables = []
    
    if strategie not in "ABCD":
      raise Exception("Strategie non valide")
    else:
      self.strategie = strategie
      
    self.nom = "Joueur "+strategie
  def Afficher(self,liste_domino):
    return [domino.Afficher() for domino in liste_domino]
  def AfficherMain(self):
    return self.nom+" " +str(self.Afficher(self.main))
  def ValeurMain(self):
    return sum([domino.Valeur() for domino in self.main])
  
  def TrouverJouables(self,n1,n2):
    for domino in self.main:
      if domino.A == n1 or domino.A == n2 or domino.B == n1 or domino.B == n2:
        self.jouables.append(domino)
        
  def TrouverJouableDoubles(self,n1,n2):
    doubles = self.TrouverDoubles()
    for domino in doubles:
      
      if domino.A == n1 or domino.A == n2 or domino.B == n1 or domino.B == n2:
        self.jouables.append(domino)
          
  def Analyser(self):
    dico = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
    for domino in self.main:
      dico[domino.A] += 1
      dico[domino.B] += 1
    return dico
  
  def TrouverDoubles(self):
    doubles = []
    for domino in self.main:
      if domino.EstDouble():
        doubles.append(domino)
    return doubles
  def TrouverMeilleur(self,liste_domino):
    L = {}
    
    if liste_domino != []:
      for domino in liste_domino:
        L[domino]=domino.Valeur()
      m = max(L.values())
      for domino,valeur in L.items():
        if valeur == m:
          return domino
    return None
  
  def Choisir(self,n1,n2):
    domino_strategie_A = []
    if self.strategie == "A":
      self.TrouverJouables(n1,n2)
      if self.jouables != []:
        d = self.TrouverMeilleur(self.jouables)
        for i in range(self.jouables.count(d)):
          domino_strategie_A.append(d)
     
        return domino_strategie_A[randint(0,len(domino_strategie_A)-1)]
      else:
        return None
      
    elif self.strategie == "B":
      self.TrouverJouables(n1,n2)
      if self.jouables != []:
        return self.jouables[randint(0,len(self.jouables)-1)]
      else:
        return None
    elif self.strategie == "C":
      self.TrouverJouables(n1,n2)
      if self.jouables != []:
        is_enough = True
    
        for valeur,nb in self.Analyser().items():
          if nb < 1:
            is_enough = False
        if is_enough:
          return self.jouables[randint(0,len(self.jouables)-1)]
        else:
          return self.jouables[randint(0,len(self.jouables)-1)]
      
    
    elif self.strategie == "D":
      self.TrouverJouableDoubles(n1,n2)
      if self.jouables != []:
        
        return self.TrouverMeilleur(self.jouables)
      else:
        self.TrouverJouables(n1,n2)
        if self.jouables != []:
          return self.TrouverMeilleur(self.jouables)
        else:
          return None
class Joueurs:
  def __init__(self,N):
    if 2 <= int(N) <= 4:
      self.N = N
    else:
      raise Exception("Nombre de joueurs non valide")
    self.listejoueurs = [Joueur(["A","B","C","D"][randint(0,3)]) for i in range(N)]
    
    self.tour = Joueur(["A","B","C","D"][randint(0,3)])
    self.Vainqueur = None
  def CommencerPartie(self):
    p1 = {}
    for joueur in self.listejoueurs:
          domino_random = joueur.main[randint(0,len(joueur.main)-1)]
        
          p1[joueur] = domino_random
    max_p1 = max([d.Valeur() for d in p1.values()])
    for joueur,domino in p1.items():
      if domino.Valeur() == max_p1:
        
        self.tour = joueur
    
    double = self.tour.TrouverDoubles()
    if double != []:
      return self.tour.TrouverMeilleur(double)
    else:
      print(self.tour.AfficherMain())
      return self.tour.main[randint(0,len(self.tour.main)-1)]
      
  
  def PasserTour(self):
    
    if (self.listejoueurs.index(self.tour)+1) < self.N:
      prochain = self.listejoueurs.index(self.tour)+1
    else:
      prochain = 0
    self.tour = self.listejoueurs[prochain]
 
  def TrouverMeilleurMain(self,n1,n2):
    j = 0
    K = {}
    for joueur in self.listejoueurs:
      joueur.jouables = []
      domino = joueur.Choisir(n1,n2)
      
      
      if joueur.main != [] and domino == None:
        j+=1
        K[joueur]= joueur.ValeurMain()
    
      
   
    
    blocage = j == self.N
    
    if blocage:
     
      joueurs_minimum_value = []
      for joueur,valeur in K.items():
        if valeur == min(K.values()):
          joueurs_minimum_value.append(joueur)
      
      if len(joueurs_minimum_value) == 1:
        return joueurs_minimum_value[0]
      else:
        return "Partie Nulle"
  
    
          
class JeuDeDominos:
  ListeDominos = [Domino(i,j) for i in range(7) for j in range(i,7)]
  def __init__(self):
    self.joueurs = Joueurs(randint(2,4))
    self.plateau = []

  def PoserPlateau(self,domino):
  
    
    if self.plateau != []:  
      premier_domino = self.plateau[0]
      dernier_domino = self.plateau[len(self.plateau)-1]
      if premier_domino.A == domino.B:
        self.plateau.insert(0,domino)
        self.joueurs.tour.main.remove(domino)
      elif premier_domino.A == domino.A:
        d = domino
        domino = domino.Retourner()
        self.plateau.insert(0,domino)
      
   
        self.joueurs.tour.main.remove(d)
       
      elif dernier_domino.B == domino.A:
        self.plateau.append(domino)
        self.joueurs.tour.main.remove(domino)
      elif dernier_domino.B == domino.B:
        d = domino
        domino_r = domino.Retourner()
        self.plateau.append(domino_r)
        p = [domino.Afficher() for domino in self.plateau]

        self.joueurs.tour.main.remove(d)
      
    else:
      self.plateau.append(domino)
      self.joueurs.tour.main.remove(domino)
      
      
    
   
    
    
  #! Passer tour 
  def FaireJouer(self,n1,n2):
    domino = self.joueurs.tour.Choisir(n1,n2)
    
    if domino != None:
     
      
      self.PoserPlateau(domino)
      self.joueurs.PasserTour()
    else:
      self.joueurs.PasserTour()
  def Distribuer(self):
    deja_distribue = []
    
    
    self.joueurs.tour = self.joueurs.listejoueurs[0] 
    z = len(self.ListeDominos)//self.joueurs.N
    
    for joueur in self.joueurs.listejoueurs:
      while len(joueur.main) != z:
        domino = self.ListeDominos[randint(0,len(self.ListeDominos)-1)]
        if domino not in deja_distribue:
          joueur.main.append(domino)
          deja_distribue.append(domino)
    
          
  def PartieFinie(self,n1,n2):
    for joueur in self.joueurs.listejoueurs:
      if joueur.main == []:
      
        self.DesignerVainqueur(joueur)
        return True
    
    
    j = self.joueurs.TrouverMeilleurMain(n1,n2)
    if j != None:
      
      self.DesignerVainqueur(j)
      return True
    
    elif j == "Partie Nulle":
      self.DesignerVainqueur("Partie Nulle")
      return True
    else:
      return False
  
  def DesignerVainqueur(self,joueur):
    
    self.joueurs.Vainqueur = joueur
      
  def LancerPartie(self):
    
    self.Distribuer()
    
    for joueur in self.joueurs.listejoueurs:
      print(joueur.AfficherMain())
    first_domino = self.joueurs.CommencerPartie()
    
    n1 = first_domino.A
    n2 = first_domino.B

    self.PoserPlateau(first_domino)
    self.joueurs.PasserTour()
 
    
    while self.PartieFinie(n1,n2) == False:
      
  
      self.FaireJouer(n1,n2)
      premier_domino = self.plateau[0]
      dernier_domino = self.plateau[len(self.plateau)-1]
      n1 = premier_domino.A
      n2 = dernier_domino.B
    if self.joueurs.Vainqueur == "Partie Nulle":
      print("Partie Nulle")
    else:
      print("Le vainqueur est ",self.joueurs.Vainqueur.nom)


def Probabilité_Gagnant_pourcentage(N):
  A = 0
  B = 0
  C = 0
  D = 0
  PNULLE = 0
  for i in range(N):
    jeu = JeuDeDominos()
    jeu.LancerPartie()
    if not jeu.joueurs.Vainqueur == "Partie Nulle":
      if jeu.joueurs.Vainqueur.strategie == "A":
        A += 1
      elif jeu.joueurs.Vainqueur.strategie == "B":
        B += 1
      elif jeu.joueurs.Vainqueur.strategie == "C":
        C += 1
      elif jeu.joueurs.Vainqueur.strategie == "D":
        D += 1
    else:
      PNULLE += 1
    
  print("Strategie A : ",A/N*100,"%")
  print("Strategie B : ",B/N*100,"%")
  print("Strategie C : ",C/N*100,"%")
  print("Strategie D : ",D/N*100,"%")
  print("Partie Nulle : ",PNULLE/N*100,"%")
  
Probabilité_Gagnant_pourcentage(1000)
  
  
    
  
  
  



  
   
    






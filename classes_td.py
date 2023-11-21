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
    return Domino(0,0)
  
  def Choisir(self,n1,n2):
    domino_strategie_A = []
    if self.strategie == "A":
      self.TrouverJouables(n1,n2)
      if self.jouables != []:
        d = self.TrouverMeilleur(self.jouables)
        for i in range(self.jouables.count(d)):
          domino_strategie_A.append(d)
          
      return domino_strategie_A[randint(0,len(domino_strategie_A)-1)]
    elif self.strategie == "B":
      self.TrouverJouables(n1,n2)
      if self.jouables != []:
        return self.jouables[randint(0,len(self.jouables)-1)]
    
    elif self.strategie == "C":
      self.TrouverJouables(n1,n2)
      if self.jouables != []:
        is_enough = True
        for valeur,nb in self.Analyser().items():
          if nb < 1:
            is_enough = False
        if is_enough:
          return self.jouables[randint(0,len(self.jouables)-1)]
        
      
    
    elif self.strategie == "D":
      self.TrouverJouableDoubles(n1,n2)
      if self.jouables != []:
        
        return self.TrouverMeilleur(self.jouables)
      else:
        self.TrouverJouables(n1,n2)
        if self.jouables != []:
          return self.TrouverMeilleur(self.jouables)

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
    toutes_les_mains = {}
    for joueur in self.listejoueurs:
      doubles = joueur.TrouverDoubles()
      print(joueur.nom,joueur.Afficher(doubles))
      toutes_les_mains[joueur]= joueur.TrouverMeilleur(doubles)
    m = max([d.Valeur() for d in toutes_les_mains.values()])
    
    for joueur,domino in toutes_les_mains.items():
      if domino.Valeur() == m:
        self.tour = joueur
        print("Le joueur ",joueur.nom," commence")
        print("Il a le domino ",domino.Afficher())
        
        return domino
  #! A revoir Problème sur self.tour str alors qu'il doit etre un joueur#
  
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
      joueur.TrouverJouables(n1,n2)
      
      if joueur.main != [] and joueur.jouables != []:
        j+=1
        K[joueur]= joueur.ValeurMain()
    
    print("K",K)
    
    blocage = j == self.N
    
    if blocage:
      for joueur,valeur in K.items():
        if valeur == min(K.values()):
          return joueur
    return None
    
          
class JeuDeDominos:
  ListeDominos = [Domino(i,j) for i in range(7) for j in range(i,7)]
  def __init__(self):
    self.joueurs = Joueurs(randint(2,4))
    self.plateau = []
  
  #! A revoir Problème sur self.tour str alors qu'il doit etre un joueur#
  def PoserPlateau(self,domino):
    self.plateau.append(domino)
    self.joueurs.tour.main.remove(domino)
    
  #! Passer tour 
  def FaireJouer(self,n1,n2):
    domino = self.joueurs.tour.Choisir(n1,n2)
    print(self.joueurs.tour.AfficherMain())
    if domino != None:
      print("Le joueur ",self.joueurs.tour.nom," joue le domino ",domino.Afficher())
      self.PoserPlateau(domino)
    else:
      self.joueurs.PasserTour()
  def Distribuer(self):
    deja_distribue = []
    
    z = 0
    if self.joueurs.N == 2:
      z = 7
    elif self.joueurs.N == 3 or self.joueurs.N == 4:
      z = 6
      
    for joueur in self.joueurs.listejoueurs:
      while len(joueur.main) < z:
        domino = JeuDeDominos.ListeDominos[randint(0,27)]
        if domino not in deja_distribue:
          joueur.main.append(domino)
          deja_distribue.append(domino)
          
  def PartieFinie(self,n1,n2):
    for joueur in self.joueurs.listejoueurs:
      if joueur.main == []:
        
        return True
      
    if self.joueurs.TrouverMeilleurMain(n1,n2):
      print("ftftftf")
      return True
    else:
      return False
  
  def DesignerVainqueur(self,joueur):
    
    self.joueurs.Vainqueur = joueur
      
  def LancerPartie(self):
    
    self.Distribuer()
    first_domino = self.joueurs.CommencerPartie()
    
    n1 = first_domino.A
    n2 = first_domino.B

    self.PoserPlateau(first_domino)
    
    p = [domino.Afficher() for domino in self.plateau]
    print(p)
    
    while self.PartieFinie(n1,n2) == False:
      
      self.FaireJouer(n1,n2)
      domino_pose = self.plateau[len(self.plateau)-1]
      n1 = domino_pose.A
      n2 = domino_pose.B
    
J = JeuDeDominos()

J.LancerPartie()

  
   
    






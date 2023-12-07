from random import randint,shuffle

class Joueur:
    def __init__(self,nom,nature):
        self.nom = nom
        if nature != "HUMAIN" and nature != "PROGRAMME":
            raise Exception("La nature du joueur doit être soit HUMAIN soit PROGRAMME")
        else:
            self.nature = nature
        
    def getInfo(self):
        return (self.nom,self.nature)
    


class Jeu:
    def __init__(self,nom="NIM",joueurs=[],allumettes=15,vainqueur=None,note =0):
        self.nom = nom
        self.joueurs = joueurs
        self.allumettes = allumettes
        self.vainqueur = vainqueur
        self.note = note
    def getInfo(self):
        return (self.nom,self.joueurs,self.allumettes,self.vainqueur,self.note)
    def Afficher(self):
        for i in range(self.allumettes):
            print("|",end=" ")
        print()
        
    def getJoueur(self):
        return self.joueurs[0]
    def getPartieFinie(self):
        return self.allumettes == 0 or self.allumettes == 1
    def setVainqueur(self,joueur):
        self.vainqueur = joueur
    def Passer(self):
        self.joueurs = [self.joueurs[1],self.joueurs[0]]
    def getCanPlay(self):
        return self.allumettes >=2
    def getSituSuivantes(self):
        liste_situation = []
        
        if self.allumettes > 3:
     
            liste_situation.append(Jeu(self.nom,self.joueurs[::-1],self.allumettes-3))
            liste_situation.append(Jeu(self.nom,self.joueurs[::-1],self.allumettes-2))
            
        elif self.allumettes == 2:
            liste_situation.append(Jeu(self.nom,self.joueurs[::-1],self.allumettes-2))
        elif self.allumettes == 3:
            liste_situation.append(Jeu(self.nom,self.joueurs[::-1],self.allumettes-3))
            liste_situation.append(Jeu(self.nom,self.joueurs[::-1],self.allumettes-2))
        return liste_situation
    
    def Max(self,liste_situation):
        m =max([situation.note for situation in liste_situation])
        for s in liste_situation:
            if s.note == m:
                return s
    def Min(self,liste_situation):
        m =min([situation.note for situation in liste_situation])
        for s in liste_situation:
            if s.note == m:
                return s

    def Eval(self):
        
        
        if self.joueurs[0].nature == "HUMAIN" and self.allumettes == 0:
          
           
            self.note = 1
        elif self.joueurs[0].nature == "PROGRAMME" and self.allumettes == 0:
         
           
            self.note = -1
        elif self.allumettes == 1:
            
            self.note = 0
            
    def minMAX(self):
       
        
        situsuiv = self.getSituSuivantes()
        for situation in situsuiv:
        
            if situation.getPartieFinie():
                
            
                
                situation.Eval()
                self.note = situation.note
                
                
                
            else:   
                situation.minMAX()
         
        if self.joueurs[0].nature == "HUMAIN":
            self.note = self.Min(situsuiv).note
        
            return self.allumettes - self.Max(situsuiv).allumettes
        elif self.joueurs[0].nature == "PROGRAMME":
            self.note = self.Max(situsuiv).note
           
            return self.allumettes - self.Min(situsuiv).allumettes          
        
    def Jouer(self):
        while not self.getPartieFinie():
            self.Afficher()
            print("Nombre d'allumettes restantes : ",self.allumettes)
            print("Tour de ",self.joueurs[0].nom)
            
            if self.joueurs[0].nature == "HUMAIN" and self.allumettes > 2:
                n = randint(2,3)
                self.allumettes -= n
               
            elif self.allumettes == 2 and self.joueurs[0].nature == "HUMAIN":
                n = 2
                self.allumettes -= n
                
            elif self.joueurs[0].nature == "PROGRAMME":
                n = self.minMAX()
                self.allumettes -= n
            self.Passer()

        if self.allumettes == 0:    
            self.setVainqueur(self.joueurs[0].nature)
           
        elif self.allumettes == 1:
            self.setVainqueur("Partie nulle")
        print(self.vainqueur," a gagne la partie")   
    
                    
        
        
        
J = Jeu("NIM",[Joueur("Bob","PROGRAMME"),Joueur("Benoit","HUMAIN")],15)
J.Jouer()

def LancerPartie(N):
    L = []
    for i in range(N):
        J1 = Joueur("Bob","PROGRAMME")
        J2 = Joueur("Benoit","HUMAIN")
        D = [J1,J2]
        for i in range(N):
            shuffle(D)
        Partie = Jeu("NIM",D,randint(10,30))
        Partie.Jouer()
        L.append(Partie.vainqueur)
    return L

class Jeu_TicTacToe:
    def __init__(self,nom="TICTACTOE",joueurs=[],plateau=[["","",""],["","",""],["","",""]],vainqueur=None,note=0):
        self.nom = nom
        self.joueurs = joueurs
        self.plateau = plateau
        self.vainqueur = vainqueur
        self.note = note
    def getInfo(self):
        return (self.nom,self.joueurs,self.plateau,self.vainqueur,self.note)
    def Afficher(self):
        for i in range(len(self.plateau)):
            print(self.plateau[i])
      
        
    def getJoueur(self):
        return self.joueurs[0]
    def getPartieFinie(self):
        for line in self.plateau:
            for case in line:
                if case == "":
                    return False
    def setVainqueur(self,joueur):
        self.vainqueur = joueur
    def Passer(self):
        self.joueurs = [self.joueurs[1],self.joueurs[0]]
    def getSituationsSuivantes(self):
        return
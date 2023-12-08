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
        if self.Check_all("O") or self.Check_all("X"):
            return True
        else:
            for i in range(len(self.plateau)):
                for j in range(len(self.plateau[i])):
                    if self.plateau[i][j] == "":
                        return False
        
    def setVainqueur(self,joueur):
        self.vainqueur = joueur
    def Passer(self):
        self.joueurs = [self.joueurs[1],self.joueurs[0]]
    def getSituationsSuivantes(self):
        liste_situation = []
        if self.getPartieFinie() == False:
            for i in range(len(self.plateau)):
                for j in range(len(self.plateau[i])):
                    if self.plateau[i][j] == "":
                        
                        copie_plateau = [line.copy() for line in self.plateau]
                        if self.joueurs[0].nature == "HUMAIN":
                            copie_plateau[i][j] = "X"
                        elif self.joueurs[0].nature == "PROGRAMME":
                            copie_plateau[i][j] = "O"
                        
                            
                        liste_situation.append(Jeu_TicTacToe(self.nom,self.joueurs[::-1],copie_plateau))
        
        if liste_situation:
            return liste_situation
        else:
            return [self]
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
        if self.Check_all("X"):
          
           
            self.note = -1
        elif self.Check_all("O"):
         
           
            self.note = 1
        elif not self.Check_all("O") and not self.Check_all("X") and self.getPartieFinie():
            
            self.note = 0
    def minMax(self):
        tous_les_plateaux_evaluer = []
        if self.getPartieFinie() == False:
            situsuiv = self.getSituationsSuivantes()
            for situation in situsuiv:
                if situation.getPartieFinie():
                    
                    situation.Afficher()
                    print("Note : ",self.note)
                    tous_les_plateaux_evaluer.append(situation.plateau)
                    return self.Eval()
                else:   
                    if situation.plateau not in tous_les_plateaux_evaluer:
                        print("ded")
                        situation.minMax()
        
            
            if self.joueurs[0].nature == "HUMAIN":
               
                self.note = self.Min(situsuiv).note
                return self.Min(situsuiv)
            elif self.joueurs[0].nature == "PROGRAMME":
                
                self.note = self.Max(situsuiv).note
                return self.Max(situsuiv)
        else:
            self.Eval()
            return self
    
        
        
        
    
    def Jouer(self):
        
        while not self.getPartieFinie():
            self.Afficher()
            print("Tour de ",self.joueurs[0].nature)
            
            if self.joueurs[0].nature == "HUMAIN":
                print("Choisissez une ligne")
                ligne = int(input())
                print("Choisissez une colonne")
                colonne = int(input())
                self.plateau[ligne][colonne] = "X"
            elif self.joueurs[0].nature == "PROGRAMME":
                p = self.minMax()
                self.plateau = p.plateau
            self.Passer()
        if self.Check_all("X"):
            self.setVainqueur("X")
        elif self.Check_all("O"):
            self.setVainqueur("O")
        elif not self.Check_all("O") and not self.Check_all("X"):
            self.setVainqueur("Partie nulle")
        print(self.vainqueur," a gagne la partie")
    def Check_all(self,signe):
        return self.Check_colonne(signe) or self.Check_line(signe) or self.Check_Diago(signe)       
    def Check_line(self,signe):
        #Check ligne
        for line in self.plateau:
            if line == [signe]*3:
                return True
        return False
        #Check colonne
    def Check_colonne(self,signe):
        t = 0
        for i in range(len(self.plateau)):
            nb_colonne_bonne = 0
            
            for j in range(len(self.plateau[i])):
                case = self.plateau[j][t]    
                if case == signe:
                    nb_colonne_bonne+=1
            if nb_colonne_bonne == 3:
                return True  
            t+=1  
        return False
    
    def Check_Diago(self,signe):
        
        nb_colonne = 0
        for i in range(len(self.plateau)):
            case = self.plateau[i][i]
            if case == signe:
                nb_colonne+=1
        
        nb_colonne2 = 0
        t = len(self.plateau)
        for i in range(len(self.plateau)):
            t-=1
            case = self.plateau[i][t]
            if case == signe:
                nb_colonne2+=1    
            
        
        if nb_colonne == 3 or nb_colonne2 == 3:
            return True
                
        return False
            
matrice = [
    ["O", "", ""],
    ["", "", ""],
    ["", "", ""]
]   

matrice_gagnante_O = [
    ["O", "X", "O"],
    ["X", "O", ""],
    ["O", "O", "X"]
]

matrice_gagnante_X = [
    ["O", "", "O"],
    ["X", "X", "X"],
    ["O", "", "X"]
]

matrice_partie_nulle = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["X", "O", "X"]
]

JT_gagnant_O = Jeu_TicTacToe("TICTACTOE", [Joueur("Bob", "PROGRAMME"), Joueur("Benoit", "HUMAIN")], matrice_gagnante_O)
JT_gagnant_X = Jeu_TicTacToe("TICTACTOE", [Joueur("Bob", "PROGRAMME"), Joueur("Benoit", "HUMAIN")], matrice_gagnante_X)
JT_partie_nulle = Jeu_TicTacToe("TICTACTOE", [Joueur("Bob", "PROGRAMME"), Joueur("Benoit", "HUMAIN")], matrice_partie_nulle)



JT = Jeu_TicTacToe("TICTACTOE",[Joueur("Bob","PROGRAMME"),Joueur("Benoit","HUMAIN")])

JT.minMax()






    


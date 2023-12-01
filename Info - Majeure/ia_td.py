class Joueur:
    def __init__(self,nom,nature):
        self.nom = nom
        if nature != "HUMAIN" or nature != "PROGRAMME":
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
    def getSituSuivantes():
        liste_situation = []
        return liste_situation
    
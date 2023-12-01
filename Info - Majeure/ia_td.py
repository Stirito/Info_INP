class Joueur:
    def __init__(self,nom,nature):
        self.nom = nom
        if nature != "HUMAIN" or nature != "PROGRAMME":
            raise Exception("La nature du joueur doit être soit HUMAIN soit PROGRAMME")
        else:
            self.nature = nature
        
    def getInfo(self):
        return (self.nom,self.nature)
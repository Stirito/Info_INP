from random import randint
from math import sqrt

longueur,largeur = 600,600
diametre = 20
rayon = diametre/2
couleur_balle = color(random(128,255),random(128,255),random(128,255))

class Vecteur:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def Scal(self,v2):
        x =self.x*v2.x
        y = self.y*v2.y
        return x+y
    def Norme(self):
        return sqrt((self.x**2+self.y**2))
    def Soust(self,v2):
        x = self.x - v2.x
        y = self.y - v2.y
        return Vecteur(x,y)
    def Mult(self,m):
        return Vecteur(m*self.x,m*self.y)
    
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Distance(self,p1,p2):
        return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    def Vect(self,p1,p2):
        return Vecteur(p2.x - p1.x, p2.y - p1.y)
    def Translater(self,v):
        return Point(self.x+v.x,self.y+v.y)

class Balle:
    def __init__(self,centre,vinst):
        self.centre = centre
        self.vinst = vinst
        self.col = couleur_balle
    def Dessiner(self):
    
        fill(self.col)
        ellipse(self.centre.x,self.centre.y,diametre,diametre)
        
        
        
    def Deplacer(self):
    
        self.centre = self.centre.Translater(self.vinst)
        
    def Rebondir(self):
        
        if self.centre.x-rayon <= 0:
            self.vinst = Vecteur(-self.vinst.x,self.vinst.y)
            self.centre.x = self.centre.x + 5
        elif longueur < self.centre.x+rayon :
            self.vinst = Vecteur(-self.vinst.x,self.vinst.y)
            self.centre.x = self.centre.x - 5
        elif largeur <= self.centre.y+rayon :
            self.vinst = Vecteur(self.vinst.x,-self.vinst.y)
            self.centre.y = self.centre.y - 5
        elif self.centre.y-rayon <= 0:
            self.vinst = Vecteur(self.vinst.x,-self.vinst.y)
            self.centre.y = self.centre.y + 5
    
class ListeBalles:
    def __init__(self,n,vmin,vmax):
        self.n = n
        self.vmin = vmin
        self.vmax = vmax
        
        self.liste_balle = [Balle(Point(randint(0,longueur),randint(0,largeur)),Vecteur(randint(vmin,vmax),randint(vmin,vmax))) for i in range(n)]
        
        self.liste_balle[0].col = color(255,0,0)
    
        for balle in self.liste_balle:
        
            for balle2 in self.liste_balle:
                if balle != balle2:
                    while balle.centre.Distance(balle.centre,balle2.centre) < diametre:
                        balle.centre = Point(randint(0,longueur),randint(0,largeur))
                        balle2.centre = Point(randint(0,longueur),randint(0,largeur))


        
    def Animer(self):
        for balle in self.liste_balle:
            
            balle.Deplacer()
            balle.Dessiner()
            balle.Rebondir()
    def EntrerCollision(self):
        for balle in self.liste_balle:
            
            for balle2 in self.liste_balle:

                if balle != balle2:
                
                    if dist(balle.centre.x,balle.centre.y,balle2.centre.x,balle2.centre.y) < 2*rayon:
                
                
                        
                    
                   
                        o1o2 = balle.centre.Vect(balle2.centre,balle.centre)
                        
                 
                    
                        n = o1o2.Mult(1/o1o2.Norme())
                        
                        
                        
                        ecart = n.Mult(diametre).Soust(o1o2)
                   
                        
                        balle.centre = balle.centre.Translater(ecart)
                        
                        
                        
                        b1 = (balle.vinst.Soust(balle2.vinst)).Scal(n)
                        new_v1 = balle.vinst.Soust(n.Mult(b1))
                        
                        b2 = (balle2.vinst.Soust(balle.vinst)).Scal(n)
                        new_v2 = balle2.vinst.Soust(n.Mult(b2))
              
                        balle.vinst = new_v1
                        balle2.vinst = new_v2
                    
                   
                    



t = ListeBalles(randint(100,101),3,4)


def setup():


    size(longueur,largeur)
    smooth()
    frameRate(60)
    background(0,0,0)
    


def draw():
    background(0,0,0)

    t.Animer()
    t.EntrerCollision()

    
    
    
    
    
    
    
    
    
        
        

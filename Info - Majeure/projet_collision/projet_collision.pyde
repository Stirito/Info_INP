from random import uniform,randint


longueur,largeur = 600,600
diametre = 20
rayon = diametre/2


class Vecteur:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def Scal(self,v2):
        return self.x*v2.x+self.y*v2.y
    def Norme(self):
        return (self.x**2+self.y**2)**1/2
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
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**1/2
    def Vect(self,p1,p2):
        return Vecteur(p2.x - p1.x, p2.y - p1.y)
    def Translater(self,v):
        return Point(self.x+v.x,self.y+v.y)

class Balle:
    def __init__(self,centre,vinst):
        self.centre = centre
        self.vinst = vinst
        self.col = color(0)
    def Dessiner(self):
        fill(self.col)
        ellipse(self.centre.x,self.centre.y,20,20)
    def Deplacer(self):
    
        self.centre.x+= self.vinst.x
        self.centre.y+=self.vinst.y
        
    def Rebondir(self):
        
        if self.centre.x-rayon <= 0:
            self.vinst = Vecteur(-self.vinst.x,self.vinst.y)
        elif longueur < self.centre.x+rayon :
            self.vinst = Vecteur(-self.vinst.x,self.vinst.y)
        elif largeur <= self.centre.y+rayon :
            self.vinst = Vecteur(self.vinst.x,-self.vinst.y)
        elif self.centre.y-rayon <= 0:
            self.vinst = Vecteur(self.vinst.x,-self.vinst.y)

class ListeBalles:
    def __init__(self,n,vmin,vmax):
        self.n = n
        self.vmin = vmin
        self.vmax = vmax
        
        self.liste_balle = [Balle(Point(randint(0,longueur),randint(0,largeur)),Vecteur(randint(vmin,vmax),randint(vmin,vmax))) for i in range(n)]
        

        
    def Animer(self):
        for balle in self.liste_balle:
            balle.Deplacer()
            balle.Dessiner()
    
            balle.Rebondir()
    def EntrerCollision(self):
        for balle in self.liste_balle:
            print(balle)
            for balle2 in self.liste_balle:
                print("2",balle)
                if not balle == balle2:
                    balle
                    o1_o2 = balle.centre.Vect().Soust(balle2.centre.Vect())
                    vnorm = o1_o2 / o1_o2.Norm()
                    if balle.centre.Distance(balle.centre,balle2.centre) <= 2*rayon:
                        print("Collision")
                        balle.col = color(random(255),random(255),random(255))
                        balle.vinst = balle.vinst - ((balle.vinst.Soust(balle2.vinst).Scal(vnorm)))
                        balle2.vinst = balle2.vinst - ((balle2.vinst.Soust(balle.vinst).Scal(vnorm)))
                


t = ListeBalles(randint(3,5),4,6)

          
def setup():


    size(600,600)
    smooth()
    frameRate(30)
    background(249,216,143)
    fill(255)
    stroke(249,216,143)

def draw():
    background(249,216,143)
    t.Animer()
    t.EntrerCollision()

    
    
    
    
        
        

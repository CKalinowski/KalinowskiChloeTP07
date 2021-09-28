from math import pi
from Cercle import Cercle

class Cylindre(Cercle):

    def __init__(self, rayon, hauteur):
        rayon = Cercle.__init__(self, rayon)
        self.hauteur = hauteur

    def volume(self):
        return round((pi *(self.rayon * self.rayon))*self.hauteur)
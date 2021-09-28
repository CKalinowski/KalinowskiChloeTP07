from math import pi
from Cylindre import Cylindre

class Cone(Cylindre):
  def __init__(self, rayon, hauteur):
    Cylindre.__init__(self, rayon, hauteur)

  def volume(self):
    #volume d’un cône = volume du cylindre correspondant divisé par 3
    return round(((pi *(self.rayon * self.rayon))*self.hauteur)/3)
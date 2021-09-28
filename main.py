print('1. Classe Cercle')

from Cylindre import Cylindre
from Cone import Cone

cyl = Cylindre(5, 7)
print(cyl.surface())
#78.54
print(cyl.volume())
#549.78

print('\n\n\n2. classe Cone')
co = Cone(5,7)
print(co.volume())
#183.26

# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

from math import sqrt  

katet1 = 3
katet2 = 2
gipotenuza = sqrt(katet1**2 + katet2**2)

ploszad = (katet1 + katet2) * 2 
print("ploszad =", ploszad)
print("gipotenuza =", gipotenuza)

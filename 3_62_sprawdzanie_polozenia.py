#!/usr/bin/env python
# coding: utf-8

xA = float(input("Podaj współrzędną x wierzchołka A trójkąta: "))
yA = float(input("Podaj współrzędną y wierzchołka A trójkąta: "))
xB = float(input("Podaj współrzędną x wierzchołka B trójkąta: "))
yB = float(input("Podaj współrzędną y wierzchołka B trójkąta: "))
xC = float(input("Podaj współrzędną x wierzchołka C trójkąta: "))
yC = float(input("Podaj współrzędną y wierzchołka C trójkąta: "))

xD = float(input("Podaj współrzędną x sprawdzanego punktu: "))
yD = float(input("Podaj współrzędną y sprawdzanego punktu: "))

def pole_trojkata(
    xA, yA,
    xB, yB, 
    xC, yC,):
    
  return abs((xB - xA) 
        * (yC - yA) 
        - (yB - yA) 
        * (xC - xA)
        ) / 2

print(pole_trojkata(xA, yA, xB, yB, xC, yC))

if (pole_trojkata(xA, yA, xB, yB, xC, yC)
    == pole_trojkata(xA, yA, xD, yD, xC, yC)
    + pole_trojkata(xA, yA, xD, yD, xB, yB)
    + pole_trojkata(xC, yC, xD, yD, xB, yB)): 
  print(True)

else: 
  print(False)


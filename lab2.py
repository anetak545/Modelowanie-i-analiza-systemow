# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:57:01 2019

@author: Paulina
"""

"""
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

print("x:")
x = int(input())
print("y:")
y = int(input())

print("-"*10)
print(x + y)
print("-"*10)

print(f"x + y: {x + y}")
print(f"x - y: {x - y}")
print(f"x * y: {x * y}")
print(f"x / y: {x / y}")
print(f"x modulo y: {x % y}")

xIsEven = x % 2 == 0
xIsEvenLog = 'X is even' if xIsEven else 'X is not even'
print(xIsEvenLog)
"""
import math as m
def zadanie1():
    X = int(input('Podaj promień X:'))
    Y = int(input('Podaj promień Y:'))

    if (X>0) and (Y>0):
        print('Obwód dla X:',obwod(X))
        print('Pole dla X:',pole(X))
        print('Obwód dla X:',obwod(Y))
        print('Pole dla X:',pole(Y))
    else:
        print('Error! Promień nie może być ujemny!\nSpróbuj ponownie')
        zadanie1()

def obwod(x):
    return(2*m.pi*x)
def pole(x):
    return(m.pi*pow(x,2))
#zadanie1()

def zadanie2():

    try:
        x = int(input('Podaj promień X:'))
        y = int(input('Podaj promień Y:'))
        if (x % y == 0) and (x % 2 == 0) and (y % 2 == 0):
            print('X jest podzielne przez Y i obie są parzyste')
        else:
            print('Spróbuj ponownie podać liczby')
            zadanie2()
    except ValueError:
        print('Zła liczba, spróbuj ponownie')
        zadanie2()
#zadanie2()
#zadanie2(10,2)    
    
def zadanie3():
    try:
        x = int(input('liczba:'))
        y = int(input('liczba:'))
        pod = x % y == 0
        podzielna = 'Jest podzielna' if pod else 'Nie jest'
        print(podzielna)
    except ValueError:
        print('Zła liczba, spróbuj ponownie')
        zadanie3()
#zadanie3()

def zadanie4():
    try: 
        x = int(input('liczba:'))
        y = int(input('liczba:'))
        if y == 0:
            print('Nie dizel przez 0')
            zadanie4()
        z = int(input('liczba:'))
        if z <= 0:
            print('Nie można')
            zadanie4()
        
        print(round(x/y,z))
    except ValueError:
        print('Zła liczba, spróbuj ponownie')
        zadanie4()
zadanie4()
#def zadanie5(x,y):
    

#print(zadanie4(5,3))
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**2*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()
"""
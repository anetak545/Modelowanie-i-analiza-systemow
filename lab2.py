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
import cs50 as cs
import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#x = cs.get_int("x: ")
#print(x)
#y = cs.get_int("y: ")
def zadanie0():
    x = cs.get_int("x: ")
    y = cs.get_int("y: ")
    return(x,y)
    
def zadanie1():
    try:
        X = int(input('Podaj promień X:'))
        Y = int(input('Podaj promień Y:'))
    
        if (X>0) and (Y>0):
            print('\nObwód dla X:',obwod(X))
            print('Pole dla X:',pole(X))
            print('Obwód dla X:',obwod(Y))
            print('Pole dla X:',pole(Y))
        else:
            print('Error! Promień nie może być ujemny!\nSpróbuj ponownie')
            zadanie1()
    except ValueError:
        print('Musisz podać liczbę całkowitą')
        zadanie1()

def obwod(x):
    return(round(2*m.pi*x,2))
def pole(x):
    return(round(m.pi*pow(x,2),2))
#zadanie1()

def zadanie2():

    try:
        x = int(input('Podaj promień X:'))
        y = int(input('Podaj promień Y:'))
        if (x % y == 0) and (x % 2 == 0) and (y % 2 == 0) and (x!=0) and (y!=0):
            print('X jest podzielne przez Y i obie są parzyste')
        elif (x % y !=0) or (x % 2 != 0) and (y % 2 != 0):
            print('X jest nie jest podzielne przez Y, albo liczby nie są parzyste!\n'
                  'Spróbuj ponownie')
            zadanie2()
        elif (x==0) or (y==0):
            print('Liczby muszą być większe od 0! Spróbuj ponownie!')
            zadanie2()
        else:
            print('Spróbuj ponownie podać liczby')
            zadanie2()
    except ValueError:
        print('Musisz podać liczbę całkowitą większą od 0, spróbuj ponownie')
        zadanie2()

#zadanie2(10,2)    
    
def zadanie3():
    try:
        x = int(input('liczba:'))
        y = int(input('liczba:'))
        if (x!=0) and (y!=0):
            pod = x % y == 0
            podzielna = 'X jest podzielna przez Y' if pod else 'X nie jest podzielna przez Y'
            print(podzielna)
        else:
            print('Musisz podać liczbę całkowitą większą od 0, spróbuj ponownie')
            zadanie3()
    except ValueError:
        print('Musisz podać liczbę całkowitą większą od 0, spróbuj ponownie')
        zadanie3()


def zadanie4():
    try: 
        x = int(input('liczba:'))
        y = int(input('liczba:'))
        if (x >0) and (y>0):
            if y == 0:
                print('Nie dizel przez 0')
                zadanie4()
            else:
                z = int(input('liczba:'))
                if z <= 0:
                    print('Nie można')
                    zadanie4()
                print(f"x / y: {round((x / y),z)})")
        else:
            print('Nie może być ujemna! Spróbuj ponownie')
            zadanie4()
        
                    
            #print("%.2f" %"x / y: {x / y}")    #%.2f% 8.833333333339
            #print(round(x/y,z))
    except ValueError:
        print('Musisz podać liczbę całkowitą większą od 0, spróbuj ponownie')
        zadanie4()

def zadanie5(x):
    try:
        if x>0:
            x_knots = np.linspace(-6*np.pi,6*np.pi,201)
            y_knots = np.linspace(-6*np.pi,6*np.pi,201)
            X, Y = np.meshgrid(x_knots, y_knots)
            R = np.sqrt(X**2+Y**2)
            Z = np.sin(x)*np.cos(R)**2*np.exp(-0.1*R)
            ax = Axes3D(plt.figure(figsize=(8,5)))
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
            plt.show()
        else:
            print('Podałes złą liczbę!')
    except ValueError:
        print('Musisz podać liczbę całkowitą większą od 0!')
        
    
#zadanie1()
#zadanie2()
#zadanie3()
#zadanie4()
#zadanie5(2)

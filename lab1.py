# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:06:16 2019

@author: Maluch
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt

#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
def zadanie1():
    y = []
    for i in range(56,101):
        y.append(2*pow(i,2)+2*i+2)
    return(y)
    
print(zadanie1())

#2 ask the user for a number and print its factorial (1p)
def zadanie2a():
    x = int(input('Podaj liczbę: '))
    return(m.factorial(x))
print(zadanie2a())

def zadanie2b():
    x = int(input('Podaj liczbę: '))
    silnia = 1
    for i in range(1,x+1):
        silnia = silnia * i
    return(silnia)
print(zadanie2b())

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
def zadanie3a(x):
    return(min(x),np.argmin(x))
print(zadanie3a([4,7,3,2,6,4]))

def zadanie3b(x):
    index = 0
    value = x[index]
    for i in range(len(x)):
        if x[i] < x[index]:
            index = i
            value = x[index]
    return(value,index)
print(zadanie3b([4,7,3,2,6,4]))

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
def zadanie4(x):
    if x > 0:
        X = np.linspace(0,x,100)
        plt.plot(X,pow(X,3))
        plt.show()
    else:
        print('Długosc nie moze byc ujemna')
        x = int(input('Podaj ponownie wartosc: '))
        zadanie4(x)
zadanie4(4)
    
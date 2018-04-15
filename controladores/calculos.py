#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sympy as sp
import math

a=sp.Symbol('a')
b=sp.Symbol('b')
c=sp.Symbol('c')
d=sp.Symbol('d')
e=sp.Symbol('e')
f=sp.Symbol('f')
g=sp.Symbol('g')
h=sp.Symbol('h')
i=sp.Symbol('i')
j=sp.Symbol('j')
k=sp.Symbol('k')
l=sp.Symbol('l')
m=sp.Symbol('m')
n=sp.Symbol('n')
o=sp.Symbol('o')
p=sp.Symbol('p')
q=sp.Symbol('q')
r=sp.Symbol('r')
s=sp.Symbol('s')
t=sp.Symbol('t')
u=sp.Symbol('u')
v=sp.Symbol('v')
w=sp.Symbol('w')
x=sp.Symbol('x')
y=sp.Symbol('y')
z=sp.Symbol('z')

variables_tuplas = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


def validar_eq(data, pi=math.pi):
    global variables_tuplas
    for variable in variables_tuplas:
        if variable in data:
            return True
    return False

def evaluar(data: str):
    return data + " = " + str(eval(data))

def Pow(a,b):
    return sp.Pow(a,b)

def integrate(data, var):
    return sp.integrate(eval(str(data)), eval(str(var)))

def derivate(data, var):
    return sp.diff(eval(str(data)), eval(str(var)))


#funciones trigonometricas
def cos(data):
    if validar_eq(str(data)):
        return sp.pretty(sp.cos(data))
    else:
        return math.cos(eval(str(data)))

def sin(data):
    if validar_eq(str(data)):
        return sp.sin()
    else:
        return math.sin(eval(str(data)))

def tan(data):
    if validar_eq(str(data)):
        return sp.tan(data)
    else:
        return math.tan(eval(str(data)))

def acos(data):
    if validar_eq(str(data)):
        return sp.acos(data)
    else:
        return math.acos(eval(str(data)))

def asin(data):
    if validar_eq(str(data)):
        return sp.asin(data)
    else:
        return math.asin(eval(str(data)))

def atan(data):
    if validar_eq(str(data)):
        return sp.atan(data)
    else:
        return math.atan(eval(str(data)))

def cosh(data):
    if validar_eq(str(data)):
        return sp.cosh(data)
    else:
        return math.cosh(eval(str(data)))

def sinh(data):
    if validar_eq(str(data)):
        return sp.sinh(data)
    else:
        return math.sinh(eval(str(data)))

def tanh(data):
    if validar_eq(str(data)):
        return sp.tanh(data)
    else:
        return math.tanh(eval(str(data)))

#exponentes
def sqrt(data):
    if validar_eq(str(data)):
        return sp.sqrt(data)
    else:
        return math.sqrt(eval(str(data)))

"""def Pow(data):
    if validar_eq(str(data)):
        return sp.Pow(data)
    else:
        return math.Pow(eval(str(data)))"""

def exp(data):
    if validar_eq(str(data)):
        return sp.exp(data)
    else:
        return math.exp(eval(str(data)))

#logaritmos
def log(data, base=10):
    if validar_eq(str(data)):
        return sp.log(data, base)
    else:
        return math.log(eval(str(data)), base)

def ln(data):
    if validar_eq(str(data)):
        return sp.log(data)
    else:
        return math.log(eval(str(data)))

#otras
def factorial(data):
    if validar_eq(str(data)):
        return sp.factorial(data)
    else:
        return math.factorial(eval(str(data)))

def simplify(data):
    if validar_eq(str(data)):
        return sp.simplify(data)
    else:
        return sp.simplify(data)

def factor(data):
    if validar_eq(str(data)):
        return sp.factor(data)
    else:
        return sp.factor(data)

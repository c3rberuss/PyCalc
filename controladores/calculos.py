#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sympy as sp


def evaluar(data: str):
    x = sp.Symbol('x')
    return data + " = " + str(eval(data))

def derivate(data):
    x = sp.Symbol('x')
    return sp.diff(eval(str(data)), x)


def Pow(a,b):
    x = sp.Symbol('x')
    return sp.Pow(a,b)

def integrate(data):
    x = sp.Symbol('x')
    return sp.integrate(eval(str(data)), x) 
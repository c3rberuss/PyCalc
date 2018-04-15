#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from controladores.botones import Acciones
from controladores import calculos as calc
import sys

app = QApplication(sys.argv)

class main(QMainWindow, Acciones):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('interfaz/mainwindow.ui', self)

        #botones numéricos
        self.btnCero.clicked.connect(self.add_n0)
        self.btnUno.clicked.connect(self.add_n1)
        self.btnDos.clicked.connect(self.add_n2)
        self.btnTres.clicked.connect(self.add_n3)
        self.btnCuatro.clicked.connect(self.add_n4)
        self.btnCinco.clicked.connect(self.add_n5)
        self.btnSeis.clicked.connect(self.add_n6)
        self.btnSiete.clicked.connect(self.add_n7)
        self.btnOcho.clicked.connect(self.add_n8)
        self.btnNueve.clicked.connect(self.add_n9)

        #botones de funciones trigonométricas
        self.btnCos.clicked.connect(self.add_cos)
        self.btnSin.clicked.connect(self.add_sin)
        self.btnTan.clicked.connect(self.add_tan)
        self.btnAcos.clicked.connect(self.add_acos)
        self.btnAsin.clicked.connect(self.add_asin)
        self.btnAtan.clicked.connect(self.add_atan)
        self.btnCosh.clicked.connect(self.add_cosh)
        self.btnSinh.clicked.connect(self.add_sinh)
        self.btnTanh.clicked.connect(self.add_tanh)

        #exponentes
        self.btnSqrt.clicked.connect(self.add_raiz)
        self.btnPow.clicked.connect(self.add_potencia)
        self.btnNotacion.clicked.connect(self.add_notacion)
        self.btnExp.clicked.connect(self.add_exp)
        
        #operadores
        self.btnMas.clicked.connect(self.add_mas)
        self.btnMenos.clicked.connect(self.add_menos)
        self.btnPor.clicked.connect(self.add_por)
        self.btnEntre.clicked.connect(self.add_entre)
        self.btnMod.clicked.connect(self.add_modulo)
        self.btnParentesis.clicked.connect(self.add_parentesis)
        
        #constantes
        self.btnPi.clicked.connect(self.add_pi)

        #integrales y derivadas
        self.btnIntegrar.clicked.connect(self.add_integral)
        self.btnDerivar.clicked.connect(self.add_derivada)

        #logaritmos
        self.btnLog.clicked.connect(self.add_log)
        self.btnLn.clicked.connect(self.add_ln)

        #otros
        self.btnFactorizar.clicked.connect(self.add_factorizar)
        self.btnSimplificar.clicked.connect(self.add_simplificar)
        self.btnAbs.clicked.connect(self.add_abs)
        self.btnFactorial.clicked.connect(self.add_factorial)
        self.btnPunto.clicked.connect(self.add_punto)

        self.btnIgual.clicked.connect(self.evaluar)   

    def evaluar(self):
        data = str(self.txtOperando.text())
        self.txtResult.append(calc.evaluar(data))

main = main()
main.show()

app.exec_()

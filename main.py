#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from controladores.botones import Acciones
from controladores import calculos as calc
import sys

from interfaz.mainwindow_interfaz import Ui_MainWindow

app = QApplication(sys.argv)

class main(QMainWindow, Acciones):

    grafica = None

    def __init__(self, grafica_):
        QMainWindow.__init__(self)
        self.grafica = grafica_

        self.grafica.setupUi(self)
        #botones numéricos
        self.grafica.btnCero.clicked.connect(self.add_n0)
        self.grafica.btnUno.clicked.connect(self.add_n1)
        self.grafica.btnDos.clicked.connect(self.add_n2)
        self.grafica.btnTres.clicked.connect(self.add_n3)
        self.grafica.btnCuatro.clicked.connect(self.add_n4)
        self.grafica.btnCinco.clicked.connect(self.add_n5)
        self.grafica.btnSeis.clicked.connect(self.add_n6)
        self.grafica.btnSiete.clicked.connect(self.add_n7)
        self.grafica.btnOcho.clicked.connect(self.add_n8)
        self.grafica.btnNueve.clicked.connect(self.add_n9)

        #botones de funciones trigonométricas
        self.grafica.btnCos.clicked.connect(self.add_cos)
        self.grafica.btnSin.clicked.connect(self.add_sin)
        self.grafica.btnTan.clicked.connect(self.add_tan)
        self.grafica.btnAcos.clicked.connect(self.add_acos)
        self.grafica.btnAsin.clicked.connect(self.add_asin)
        self.grafica.btnAtan.clicked.connect(self.add_atan)
        self.grafica.btnCosh.clicked.connect(self.add_cosh)
        self.grafica.btnSinh.clicked.connect(self.add_sinh)
        self.grafica.btnTanh.clicked.connect(self.add_tanh)

        #exponentes
        self.grafica.btnSqrt.clicked.connect(self.add_raiz)
        self.grafica.btnPow.clicked.connect(self.add_potencia)
        self.grafica.btnNotacion.clicked.connect(self.add_notacion)
        self.grafica.btnExp.clicked.connect(self.add_exp)
        
        #operadores
        self.grafica.btnMas.clicked.connect(self.add_mas)
        self.grafica.btnMenos.clicked.connect(self.add_menos)
        self.grafica.btnPor.clicked.connect(self.add_por)
        self.grafica.btnEntre.clicked.connect(self.add_entre)
        self.grafica.btnMod.clicked.connect(self.add_modulo)
        self.grafica.btnParentesis.clicked.connect(self.add_parentesis)
        
        #constantes
        self.grafica.btnPi.clicked.connect(self.add_pi)

        #integrales y derivadas
        self.grafica.btnIntegrar.clicked.connect(self.add_integral)
        self.grafica.btnDerivar.clicked.connect(self.add_derivada)

        #logaritmos
        self.grafica.btnLog.clicked.connect(self.add_log)
        self.grafica.btnLn.clicked.connect(self.add_ln)

        #otros
        self.grafica.btnFactorizar.clicked.connect(self.add_factorizar)
        self.grafica.btnSimplificar.clicked.connect(self.add_simplificar)
        self.grafica.btnAbs.clicked.connect(self.add_abs)
        self.grafica.btnFactorial.clicked.connect(self.add_factorial)
        self.grafica.btnPunto.clicked.connect(self.add_punto)
        self.grafica.btnIgual.clicked.connect(self.evaluar)   

    def evaluar(self):
        data = str(self.grafica.txtOperando.text())
        self.grafica.txtResult.append(calc.evaluar(data))


interfaz = Ui_MainWindow()
main = main(interfaz)

main.show()

app.exec_()

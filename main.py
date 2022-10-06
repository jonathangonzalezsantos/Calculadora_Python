# -*- coding: utf-8 -*-
"""
Módulo principal da aplicación
"""


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src import calculadora
from src import fiestras

import sys
import re
import time


class miCalculadora (QMainWindow):

    def __init__(self, parent=None):
        """"Constructor da clase
        
        Móstrase a calculadora cos seus correspondentes componentes:

        - Reinicialízase o lineEditResultado a 0.
        - Cárganse as iconas dos botóns da calculadora.
        - Especifícanse todos os slots-signals correspondentes aos botóns da calculadora e ao menú
        """
        QMainWindow.__init__(self, parent)
        self.ui = calculadora.Ui_MainWindow()
        self.ui.setupUi(self.ui)
        self.ui.show()
        self.ui.setWindowTitle("Calculadora para nenos")

        self.ui.menuInformacion.setToolTipsVisible(True)
        self.ui.menuOpcions.setToolTipsVisible(True)
        self.ui.lineEditResultado.setText("0")


        self.ui.pushButton0.clicked.connect(self.digitoPulsado)
        self.ui.pushButton1.clicked.connect(self.digitoPulsado)
        self.ui.pushButton2.clicked.connect(self.digitoPulsado)
        self.ui.pushButton3.clicked.connect(self.digitoPulsado)
        self.ui.pushButton4.clicked.connect(self.digitoPulsado)
        self.ui.pushButton5.clicked.connect(self.digitoPulsado)
        self.ui.pushButton6.clicked.connect(self.digitoPulsado)
        self.ui.pushButton7.clicked.connect(self.digitoPulsado)
        self.ui.pushButton8.clicked.connect(self.digitoPulsado)
        self.ui.pushButton9.clicked.connect(self.digitoPulsado)
        self.ui.pushButtonComa.clicked.connect(self.botonPulsadoComa)
        self.ui.pushButtonSuma.clicked.connect(self.botonPulsadoSuma)
        self.ui.pushButtonResta.clicked.connect(self.botonPulsadoResta)
        self.ui.pushButtonMultiplicacion.clicked.connect(self.botonPulsadoMulti)
        self.ui.pushButtonDivision.clicked.connect(self.botonPulsadoDiv)
        self.ui.pushButtonIgual.clicked.connect(self.botonPulsadoIgual)
        self.ui.pushButtonLimpar.clicked.connect(self.botonPulsadoLimpar)
        self.ui.pushButtonRetroceso.clicked.connect(self.botonPulsadoBorrar)


        self.ui.actionSair.triggered.connect(self.salir)
        self.ui.actionLimpar.triggered.connect(self.botonPulsadoLimpar)
        self.ui.actionSobreAapp.triggered.connect(self.sobreApp)
        self.ui.actionManual.triggered.connect(self.manual)

    def salir(self):
        """Método que nos mostra unha pequena fiestra consultando se confirmamos a saída da app. Mostra a chamada á clase Ui_Sair do arquivo fiestras.py"""
        MainSair.show()

    def manual(self):
        """Método que nos mostra o manual da app en PDF. Mostra a chamada á clase PdfWindow do arquivo fiestras.py.
        
        Ao método pasámoslle a ruta do arquivo como argumento"""
        self.arquivoPdf = fiestras.PdfWindow(self)
        self.arquivoPdf.showPdf("docs/build/latex/calculadoraparanenos.pdf")

    def sobreApp(self):
        """Método que nos mostra unha pequena fiestra cos datos da App. Mostra a chamada á clase Ui_info do arquivo fiestras.py"""
        MainInfo.show()

    def botonPulsadoIgual(self):
        """Método co que se fai a operación escrita no label da operación.
        No caso de que o resultado obtido teña máis de 10 decimales, redondéase a 8 decimales.
        
        No caso de que o resultado obtido teña unha lonxitude de máis de 30 díxitos a operación non se realizará, mostrarase un aviso/erro, suspenderase tres segundos a app e reiniciarase
        
        No caso de que se produza un erro matemático, mostrarase un aviso/erro, suspenderase tres segundos a app e reiniciarse."""
        
        texto = self.ui.labelOperacion.text()

        if (len(texto)==0):
            pass
        else:
            try:
                while texto[0] == '0':
                    patron = re.compile(r'[.]')
                    if (patron.search(texto) == None):
                        texto = texto[1:]
                    else:
                        break

                resultado = eval(texto)
                if (len(str(resultado)) > 10):
                    resultadoDecimalCurto = round(resultado, 8)
                    self.ui.lineEditResultado.setText(str(resultadoDecimalCurto))
                else:
                    self.ui.lineEditResultado.setText(str(resultado))

                if (len(str(resultado)) > 30):
                    self.ui.lineEditResultado.setText("OPERACIÓN MOI COMPLICADA PARA UN CATIVO. REINICIÁNDOSE...")
                    print("Operación moi longa. A aplicación mostrará mensaxe de erro ao usuario, bloquearase 3 segundos e limparase.")
                    time.sleep(3)
                    self.botonPulsadoLimpar()
                
            except:
                self.ui.lineEditResultado.setText("ERRO NA OPERACIÓN. REINICIÁNDOSE...")
                print("Erro na operación. A aplicación mostrará mensaxe de erro ao usuario, bloquearase 3 segundos e limparase.")
                time.sleep(3)
                self.botonPulsadoLimpar()

        self.ui.labelOperacion.setText("")

    def botonPulsadoLimpar(self):
        """Método có que se limpa/reinicializa a calculadora"""
        entrada = ""
        self.ui.labelOperacion.setText(entrada)
        self.ui.lineEditResultado.setText("0")

    def botonPulsadoBorrar(self):
        """"Método co que se borra o último díxito/caracter engadido no label da Operación"""
        entrada = self.ui.labelOperacion.text()
        self.ui.labelOperacion.setText(entrada[:len(entrada)-1])

    def digitoPulsado(self):
        """Método que engade o díxito que se pulse ou escriba co teclado."""
        botonQueChama = self.sender().objectName()
        numero = botonQueChama[len(botonQueChama)-1]
        entrada = self.ui.labelOperacion.text()
        entrada += numero
        self.ui.labelOperacion.setText(entrada)

    def botonPulsadoSuma(self):
        """Método que engade o símbolo da suma á operación.
        
        No caso de que o último caracter indicado no label da operación sexa un punto ou outro símbolo de operación, sobrescríbese para evitar erros matemáticos.
        """
        if (self.ui.labelOperacion.text() == ""):
            entrada = self.ui.lineEditResultado.text()
        else:
            entrada = self.ui.labelOperacion.text()
        if (entrada[len(entrada) - 1] == "+" or entrada[len(entrada) - 1] == "-" or entrada[len(entrada) - 1] == "*" or entrada[len(entrada) - 1] == "/" or entrada[len(entrada) - 1] == "."):
            entrada = entrada[:-1]
        entrada += "+"
        self.ui.labelOperacion.setText(entrada)

    def botonPulsadoMulti(self):
        """Método que engade o símbolo da multiplicación á operación.
        
        No caso de que o último caracter indicado no label da operación sexa un punto ou outro símbolo de operación, sobrescríbese para evitar erros matemáticos.
        """
        if (self.ui.labelOperacion.text() == ""):
            entrada = self.ui.lineEditResultado.text()
        else:
            entrada = self.ui.labelOperacion.text()
        if (entrada[len(entrada) - 1] == "+" or entrada[len(entrada) - 1] == "-" or entrada[len(entrada) - 1] == "*" or entrada[len(entrada) - 1] == "/" or entrada[len(entrada) - 1] == "."):
            entrada = entrada[:-1]
        entrada += "*"
        self.ui.labelOperacion.setText(entrada)

    def botonPulsadoResta(self):
        """Método que engade o símbolo da resta á operación.
        
        No caso de que o último caracter indicado no label da operación sexa un punto ou outro símbolo de operación, sobrescríbese para evitar erros matemáticos.
        """
        if (self.ui.labelOperacion.text() == ""):
            entrada = self.ui.lineEditResultado.text()
        else:
            entrada = self.ui.labelOperacion.text()
        if (entrada[len(entrada) - 1] == "+" or entrada[len(entrada) - 1] == "-" or entrada[len(entrada) - 1] == "*" or entrada[len(entrada) - 1] == "/" or entrada[len(entrada) - 1] == "."):
            entrada = entrada[:-1]
        entrada += "-"
        self.ui.labelOperacion.setText(entrada)

    def botonPulsadoDiv(self):
        """Método que engade o símbolo da división á operación.
        
        No caso de que o último caracter indicado no label da operación sexa un punto ou outro símbolo de operación, sobrescríbese para evitar erros matemáticos.
        """
        if (self.ui.labelOperacion.text() == ""):
            entrada = self.ui.lineEditResultado.text()
        else:
            entrada = self.ui.labelOperacion.text()
        if (entrada[len(entrada) - 1] == "+" or entrada[len(entrada) - 1] == "-" or entrada[len(entrada) - 1] == "*" or entrada[len(entrada) - 1] == "/" or entrada[len(entrada) - 1] == "."):
            entrada = entrada[:-1]
        entrada += "/"
        self.ui.labelOperacion.setText(entrada)

    def botonPulsadoComa(self):
        """ Método chamado cada vez que se pulsa o botón decimal ou se pulsa no teclado o punto (.).

        O método comproba:

        - Se o label onde se recolle a operación está vacío, recolle o 0 do lineEdit onde está o resultado (iníciase con un 0)
        - Se o último caracter é un símbolo de operación sobrescríbeo, sempre que sexa posible (no caso de que non teña o díxito un punto xa escrito)
        - Se o número que estase a escribir no label da operación xa ten punto non permite poñer outro para evitar erros matemáticos.
        """
        if (self.ui.labelOperacion.text() == ""):
            entrada = self.ui.lineEditResultado.text()
        else:
            entrada = self.ui.labelOperacion.text()
        if (entrada[len(entrada) - 1] == '+' or entrada[len(entrada) - 1] == '-' or entrada[len(entrada) - 1] == '*' or entrada[len(entrada) - 1] == '/' or entrada[len(entrada) - 1] == '.'):
                entrada = entrada[:-1]
        comas = 0
        signos = 0
        patron = re.compile(r'[.]')
        if (patron.search(entrada) == None):
            entrada += "."
            comas = comas + 1
        else:
            pass
        for i in entrada:
            if i == '.':
                comas = comas + 1
            if i == '*' or i == '-' or i == '+' or i == '/':
                signos = signos + 1
        if (signos >= comas):
            entrada += '.'
        else:
            pass
        self.ui.labelOperacion.setText(entrada)


if __name__ == "__main__":
    """Método de carga inicial da aplicación"""
    app = QApplication(sys.argv)
    calculadora_nueva = miCalculadora()
    MainInfo = fiestras.Ui_Info()
    MainSair = fiestras.Ui_Sair()
    app.exec_()
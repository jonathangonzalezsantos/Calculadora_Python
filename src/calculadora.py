# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from src.botons import *


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(747, 538)
        MainWindow.setMinimumSize(QSize(747, 538))
        MainWindow.setMaximumSize(QSize(747, 538))
        icon = QIcon()
        icon.addFile(u"../../resources/icons/calculadora.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(True)

        #Creación do Menú
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 24))
        self.menuOpcions = QMenu(self.menubar)
        self.menuOpcions.setObjectName(u"menuOpcions")
        self.menuInformacion = QMenu(self.menubar)
        self.menuInformacion.setObjectName(u"menuInformacion")
        MainWindow.setMenuBar(self.menubar)

        #Accións que corresponderán aos botós do menú
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.actionManual = QAction(MainWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.actionSobreAapp = QAction(MainWindow)
        self.actionSobreAapp.setObjectName(u"actionSobreAapp")
        self.actionLimpar = QAction(MainWindow)
        self.actionLimpar.setObjectName(u"actionLimpar")

        #Engádense accións aos botós do menú
        self.menubar.addAction(self.menuOpcions.menuAction())
        self.menubar.addAction(self.menuInformacion.menuAction())
        self.menuOpcions.addAction(self.actionLimpar)
        self.menuOpcions.addAction(self.actionSair)
        self.menuInformacion.addAction(self.actionManual)
        self.menuInformacion.addAction(self.actionSobreAapp)


        #Creación de Layouts
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 120, 471, 381))

        self.LayoutNumeros = QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutNumeros.setObjectName(u"LayoutNumeros")
        self.LayoutNumeros.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.LayoutNumeros.addLayout(self.horizontalLayout)
        self.LayoutNumeros.addLayout(self.horizontalLayout_3)
        self.LayoutNumeros.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(490, 380, 251, 121))

        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(490, 10, 251, 361))
        self.gridLayoutOperaciones = QGridLayout(self.gridLayoutWidget)
        self.gridLayoutOperaciones.setSpacing(0)
        self.gridLayoutOperaciones.setObjectName(u"gridLayoutOperaciones")
        self.gridLayoutOperaciones.setContentsMargins(0, 0, 0, 0)


        #Creación de botóns de formación de díxitos. Créanse coa clase BotonNumero que extende de QPushButton. Engádense aos respectivos layouts
        self.pushButton7 = BotonNumero(self.verticalLayoutWidget, "7", "resources/icons/7.png")
        self.horizontalLayout_2.addWidget(self.pushButton7)
        self.pushButton8 = BotonNumero(self.verticalLayoutWidget, "8", "resources/icons/8.png")
        self.horizontalLayout_2.addWidget(self.pushButton8)
        self.pushButton9 = BotonNumero(self.verticalLayoutWidget, "9", "resources/icons/9.png")
        self.horizontalLayout_2.addWidget(self.pushButton9)
        self.pushButton4 = BotonNumero(self.verticalLayoutWidget, "4", "resources/icons/4.png")
        self.horizontalLayout_3.addWidget(self.pushButton4)
        self.pushButton5 = BotonNumero(self.verticalLayoutWidget, "5", "resources/icons/5.png")
        self.horizontalLayout_3.addWidget(self.pushButton5)
        self.pushButton6 = BotonNumero(self.verticalLayoutWidget, "6", "resources/icons/6.png")
        self.horizontalLayout_3.addWidget(self.pushButton6)
        self.pushButton1 = BotonNumero(self.verticalLayoutWidget, "1", "resources/icons/1.png")
        self.horizontalLayout.addWidget(self.pushButton1)
        self.pushButton2 = BotonNumero(self.verticalLayoutWidget, "2", "resources/icons/2.png")
        self.horizontalLayout.addWidget(self.pushButton2)
        self.pushButton3 = BotonNumero(self.verticalLayoutWidget, "3", "resources/icons/3.png")
        self.horizontalLayout.addWidget(self.pushButton3)
        self.pushButton0 = BotonNumero(self.horizontalLayoutWidget_4, "0", "resources/icons/0.png")
        self.horizontalLayout_4.addWidget(self.pushButton0)
        self.pushButtonComa = BotonNumero(self.horizontalLayoutWidget_4, "Punto", "resources/icons/dec.png")
        self.horizontalLayout_4.addWidget(self.pushButtonComa)

        #Creación de botóns de operacións. Créanse coa clase BotonOperacion que extende de QPushButton. Engádense aos respectivos layouts
        self.pushButtonSuma = BotonOperacion(self.gridLayoutWidget, "Suma", "resources/icons/+.png", "+")
        self.gridLayoutOperaciones.addWidget(self.pushButtonSuma, 1, 0, 1, 1)
        self.pushButtonResta = BotonOperacion(self.gridLayoutWidget, "Resta", "resources/icons/-.png", "-")
        self.gridLayoutOperaciones.addWidget(self.pushButtonResta, 1, 1, 1, 1)
        self.pushButtonMultiplicacion = BotonOperacion(self.gridLayoutWidget, "Multiplicacion", "resources/icons/x.png", "x")
        self.gridLayoutOperaciones.addWidget(self.pushButtonMultiplicacion, 2, 0, 1, 1)
        self.pushButtonIgual = BotonOperacion(self.gridLayoutWidget, "Igual", "resources/icons/=.png", "=")
        self.gridLayoutOperaciones.addWidget(self.pushButtonIgual, 3, 0, 1, 2)
        self.pushButtonDivision = BotonOperacion(self.gridLayoutWidget, "Division", "resources/icons/div.png", "/")
        self.gridLayoutOperaciones.addWidget(self.pushButtonDivision, 2, 1, 1, 1)

        #Creación de botóns de corrección. Créanse coa clase BotonCorrexir que extende de QPushButton. Engádense aos respectivos layouts
        self.pushButtonLimpar = BotonCorrexir(self.gridLayoutWidget, "Limpar", "resources/icons/c.png")
        self.gridLayoutOperaciones.addWidget(self.pushButtonLimpar, 0, 0, 1, 1)
        self.pushButtonRetroceso = BotonCorrexir(self.gridLayoutWidget, "Retroceso", "resources/icons/borrar.png")
        self.gridLayoutOperaciones.addWidget(self.pushButtonRetroceso, 0, 1, 1, 1)


        #Creación do lineEdit onde se recolle o resultado
        self.lineEditResultado = QLineEdit(self.centralwidget)
        self.lineEditResultado.setObjectName(u"lineEditResultado")
        self.lineEditResultado.setEnabled(False)
        self.lineEditResultado.setGeometry(QRect(12, 56, 471, 51))
        self.lineEditResultado.setToolTip(u"Neste recadro mostrase o resultado")
        self.lineEditResultado.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditResultado.setStyleSheet("color: rgb(100,100,100)")


        #Creación do label onde se mostra a operación que se está a escribir
        self.labelOperacion = QLabel(self.centralwidget)
        self.labelOperacion.setObjectName(u"labelOperacion")
        self.labelOperacion.setGeometry(QRect(16, 10, 461, 41))
        self.labelOperacion.setToolTip(u"Neste recadro mostrase a operacio que estas a escribir")
        self.labelOperacion.setLayoutDirection(Qt.RightToLeft)
        self.labelOperacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.actionSair.setToolTip(QCoreApplication.translate("MainWindow", u"Pulsa aqui para sair da calculadora", None))
        self.actionManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.actionManual.setToolTip(QCoreApplication.translate("MainWindow", u"Descarga do manual da calculadora", None))
        self.actionSobreAapp.setText(QCoreApplication.translate("MainWindow", u"Sobre a app", None))
        self.actionSobreAapp.setToolTip(QCoreApplication.translate("MainWindow", u"Abre outra fiestra con informacion da app", None))
        self.actionLimpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.actionLimpar.setToolTip(QCoreApplication.translate("MainWindow", u"Limpa a calculadora", None))
        self.pushButtonIgual.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.labelOperacion.setText("")
        self.menuOpcions.setTitle(QCoreApplication.translate("MainWindow", u"Opcions", None))
        self.menuInformacion.setTitle(QCoreApplication.translate("MainWindow", u"Informacion", None))
    # retranslateUi



# -*- coding: utf-8 -*-
"""
Módulo no que se cargan as fiestras dos botós do menubar da aplicación: información sobre a app e manual en PDF.
"""

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

import sys


class PdfWindow(QMainWindow):
    """ Clase coa que cargamos o manual en PDF"""

    def __init__(self, parent=None):
        """Construtor da clase."""
        super(PdfWindow, self).__init__(parent)
        self.setWindowTitle("Calculadora para nenos")
        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.web.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.setCentralWidget(self.web)

    def showPdf(self, ruta: str):
        """Método que recibe a ruta do ficheiro PDF que queremos visualizar.

        Args:
            ruta (str): Ruta ao ficheiro PDF que queremos amosar
        """
        try:
            absolute_path = QFileInfo(ruta).absoluteFilePath()
            url_to_manual = QUrl.fromLocalFile(absolute_path)
            self.web.load(url_to_manual)
            self.showMaximized()
        except Exception as e:
            print(str(e))

class AboutWindow(QMainWindow):
    """ Fiestra secundaria na que se amosa a información referente á aplicación"""

    def __init__(self, parent=None):
        """Construtor da clase."""
        super(AboutWindow, self).__init__(parent)
        self.setWindowTitle(Options.TR_("Sobre a aplicación"))
        self.setGeometry(400, 350, 300, 140)

        vbox_layout = QVBoxLayout()
        self.label_title = QLabel(Options.__PROJECT__)
        self.label_title.setStyleSheet("font: 30pt Comic Sans MS")
        self.label_author = QLabel(Options.__AUTHOR__)
        self.label_license = QLabel(Options.__LICENSE__ + " " + Options.__VERSION__)
        self.label_email = QLabel(Options.__EMAIL__)
        self.data_widget = QWidget()
        vbox_layout.addWidget(self.label_title)
        vbox_layout.addWidget(self.label_author)
        vbox_layout.addWidget(self.label_license)
        vbox_layout.addWidget(self.label_email)
        self.data_widget.setLayout(vbox_layout)

        self.label_image = QLabel()
        pixmap = QPixmap(Options.__LOGO__)
        pixmap = pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(pixmap)

        self.central_widget = QWidget()
        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.label_image)
        hbox_layout.addSpacing(30)
        hbox_layout.addWidget(self.data_widget)
        self.central_widget.setLayout(hbox_layout)

        self.setCentralWidget(self.central_widget)

class Ui_Info(QMainWindow):
    """ Fiestra na que se amosa a información da app"""
    
    def __init__(self, parent=None):
        """Constructor da clase"""
        super(Ui_Info, self).__init__(parent)
        self.resize(350, 150)
        self.setMinimumSize(QSize(350, 150))
        self.setMaximumSize(QSize(350, 150))
        self.setWindowTitle("Información")
        centralwidget = QWidget(self)
        self.lAutor = QLabel(centralwidget)
        self.lAutor.setText("App creada por: Jonathan Glez.")
        self.lAutor.setGeometry(QRect(10, 10, 500, 31))
        self.lFecha = QLabel(centralwidget)
        self.lFecha.setText("Data: 16/04/2021")
        self.lFecha.setGeometry(QRect(10, 40, 351, 31))
        self.lVersion = QLabel(centralwidget)
        self.lVersion.setGeometry(QRect(10, 70, 81, 71))
        self.lVersion.setText("v1.0")
        self.setCentralWidget(centralwidget)

class Ui_Sair(QMainWindow):
    """ Fiestra emerxente na que se pregunta ao usuario si realmente quere saír da app"""

    def __init__(self, parent=None):
        """Constructor da clase"""
        super(Ui_Sair, self).__init__(parent)
        self.resize(300, 100)
        self.setMinimumSize(QSize(300, 100))
        self.setMaximumSize(QSize(300, 100))
        self.setWindowTitle("Saída da calculadora")
        centralwidget = QWidget(self)
        self.lTexto = QLabel(centralwidget)
        self.lTexto.setText("¿Confirma que quere saír da calculadora?")
        self.lTexto.setGeometry(QRect(10, 10, 300, 30))
        self.pbSi = QPushButton(centralwidget)
        self.pbSi.setText("SÍ")
        self.pbSi.setGeometry(10 , 60, 40, 30)
        self.pbNo = QPushButton(centralwidget)
        self.pbNo.setText("NON")
        self.pbNo.setGeometry(QRect(60, 60, 40, 30))
        self.setCentralWidget(centralwidget)


        self.pbSi.clicked.connect(self.pulsadoSi)
        self.pbNo.clicked.connect(self.pulsadoNo)

    def pulsadoSi(self):
        """Método que pecha a app"""
        sys.exit()

    def pulsadoNo(self):
        """Método para ocultar a fiestra de sair da app"""
        self.hide()
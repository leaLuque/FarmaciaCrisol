# -*- coding:utf-8 -*-
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

from gui import MdiWidget
from ventanas.vtnAyuda import Ui_vtnAyuda

class Ayuda (MdiWidget, Ui_vtnAyuda):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        view = QWebView(self)
        view.load(QUrl("file:///home/waldo/Documentos/FarmaciaCrisol/web/index.html"))
        view.show()
        self.verticalLayout.addWidget(view)
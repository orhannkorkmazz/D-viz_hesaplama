import sys
import requests
import sqlite3
from PyQt5 import  QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):
        
        self.döviz_birimi=QtWidgets.QLineEdit()
        self.miktar=QtWidgets.QLineEdit()
        self.euro = QtWidgets.QPushButton("Euro üzerinden")
        self.usd = QtWidgets.QPushButton("Dolar üzerinden")
        self.yazi_alani1 = QtWidgets.QLabel("Çevirmek istediğini döviz birimini giriniz:")
        self.yazi_alani2 = QtWidgets.QLabel("Çevirmek istediğini döviz miktarını giriniz:")
        self.yazi_alani3 = QtWidgets.QLabel("Çevrilen miktarın karşılığı:")
        
        hbox=QtWidgets.QHBoxLayout()
        hbox.addStretch()
        
        hbox.addWidget(self.euro)
        hbox.addWidget(self.usd)
        
        hbox.addStretch()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(QtWidgets.QLabel("Döviz Birimi:"))
       
        v_box.addWidget(self.döviz_birimi)
        v_box.addWidget(QtWidgets.QLabel("Miktar:"))
        v_box.addWidget(self.miktar)
        
        v_box.addWidget(self.yazi_alani3)
        v_box.addStretch()
        v_box.addLayout(hbox)
        self.setLayout(v_box)
        self.setWindowTitle("Exchange")
        self.euro.clicked.connect(self.euro_hesapla)
        self.usd.clicked.connect(self.usd_hesapla)
        self.show()
    def euro_hesapla(self):
        
        url_eur = "http://data.fixer.io/api/latest?access_key=03361625a2a57ba1be4a0151e7a04794&format=1&_gl=1*1femyhn*_ga*NjU2NTYyMTY2LjE2ODg0OTIyNzg.*_ga_HGV43FGGVM*MTY4ODQ5NjI1NS4yLjEuMTY4ODQ5NjYwNS4yMC4wLjA."
        response=requests.get(url_eur)

        json_veri=response.json()
        text1 = self.miktar.text()
        text2 = self.döviz_birimi.text()
        girilen_döviz=str(text2)
        girilen_miktar=float(text1)
        try:
            sonuc = json_veri['rates'][girilen_döviz] * girilen_miktar
            self.yazi_alani3.setText(str(sonuc))
        except KeyError:
            self.yazi_alani3.setText("Lütfen uygun değerler girdiğinizden emin olun")
    def usd_hesapla(self):
        
        url_usd = "http://data.fixer.io/api/latest?access_key= 03361625a2a57ba1be4a0151e7a04794"#Dolardan diğer birimlere çeviren api key yok ondan dolayı düzgün çalışmaz dolar kuru
        response=requests.get(url_usd)

        json_veri=response.json()
        text1 = self.miktar.text()
        text2 = self.döviz_birimi.text()
        girilen_döviz=str(text2)
        girilen_miktar=float(text1)
        try:
            sonuc = json_veri['rates'][girilen_döviz] * girilen_miktar
            self.yazi_alani3.setText(str(sonuc))
        except KeyError:
            self.yazi_alani3.setText("Lütfen uygun değerler girdiğinizden emin olun")
        
            
 
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())

# pip install pyqt5
# pyuic5 designer.ui -o design.py  = Gera o arquivo python do feito em pqt5 no
# qt designer


import sys
from validacpf import valida_cpf
from geradorcpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow

print(gera_cpf())


import design


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setStyleSheet(
            "color: green;"
        )
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        
        self.labelRetorno.setStyleSheet(
            "color: green;" if valida_cpf(cpf) else "color: red;"
        )
        
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()

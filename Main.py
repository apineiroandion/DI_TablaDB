import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableView

from Modelo_Tabla import Modelo_Tabla


class ExemploQTableView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo QTableView")

        self.datos = [['Nome','DNI','Xenero','Falecido'],
                      ['Ana Perez','123456798X','Muller',False],
                      ['Paco Porras','798456123D','Home',True],
                      ['Lina Saiz','46512379Q','Home',False],
                      ['Roque Vila','147852369W','Muller',True]]

        caixa = QVBoxLayout()
        self.tvwtabla = QTableView()
        modelo = Modelo_Tabla(self.datos)
        self.tvwtabla.setModel(modelo)
        self.tvwtabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        caixa.addWidget(self.tvwtabla)

        container = QWidget()
        container.setLayout(caixa)
        self.setCentralWidget(container)
        self.setFixedSize(400, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ExemploQTableView()
    app.exec()
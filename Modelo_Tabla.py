from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QBrush


class Modelo_Tabla (QAbstractTableModel):
    # Constructor
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla # Guardamos la tabla en un atributo

    # Este metodo es llamado por la vista para obtener el numero de filas
    def rowCount(self, index):
        return len(self.tabla)

    # Este metodo es llamado por la vista para obtener el numero de columnas
    def columnCount(self, index):
        return len(self.tabla[0])

    # Este metodo es llamado por la vista para obtener los datos de la tabla
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.tabla[index.row()][index.column()]
        # si es hombre poner el color de fondo en azul
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[index.row()][2] == 'Home' and self.tabla[index.row()][3] == False:
                return QBrush(Qt.GlobalColor.blue)
            if self.tabla[index.row()][2] == 'Muller' and self.tabla[index.row()][3] == False:
                return QBrush(Qt.GlobalColor.magenta)
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[index.row()][3] == True:
                return QBrush(Qt.GlobalColor.red)
        return None
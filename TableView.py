import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout, QAbstractItemView, QHeaderView
from PyQt6.QtCore import QAbstractTableModel, Qt

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self._data.columns[section]
        else:
            return str(section)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Pandas DataFrame Viewer')

        # create sample data
        data = {'Name': ['John', 'Emily', 'Sam', 'Jessica'],
                'Age': [32, 25, 47, 18],
                'City': ['New York', 'Paris', 'London', 'Tokyo']}
        df = pd.DataFrame(data)

        # create table view widget
        table_view = QTableView(self)
        table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table_model = PandasModel(df)
        table_view.setModel(table_model)

        # create layout and add table view
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

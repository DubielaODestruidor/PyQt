import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout, QAbstractItemView, QHeaderView, QPushButton
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex

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
        self.df = pd.DataFrame(data)

        # create table view widget
        self.table_view = QTableView(self)
        self.table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_model = PandasModel(self.df)
        self.table_view.setModel(self.table_model)

        # create refresh button
        self.refresh_button = QPushButton('Refresh', self)
        self.refresh_button.clicked.connect(self.refresh_view)

        # create layout and add table view and button
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)
        layout.addWidget(self.refresh_button)
        self.setLayout(layout)

    def refresh_view(self):
        # update data in DataFrame
        self.df.iloc[1, 1] = 26
        self.df.iloc[2, 2] = 'Paris'

        # update view by emitting dataChanged signal
        self.table_model.dataChanged.emit(QModelIndex(), QModelIndex())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

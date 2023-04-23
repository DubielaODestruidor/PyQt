import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, \
    QLineEdit, QPushButton

itens = ["Teste item 1", "Teste item 2"]


# Ainda não faz nada
def parametros_de_busca():
    item1 = window.drop_busca_inicio.currentText()
    item2 = window.drop_busca_fim.currentText()
    digitado = window.search.text()
    print(f'{item1} - {item2} - {digitado}')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Create a tab widget and a tab for your layout
        tab_widget = QTabWidget()
        tab_personalizada = QWidget()
        tab_careca = QWidget()
        tab_widget.addTab(tab_personalizada, "Personalizada")
        tab_widget.addTab(tab_careca, "Careca")

        # Create your layout
        label = QLabel("Personalizada")
        drop_busca_inicio = QComboBox()
        drop_busca_inicio.addItem(itens[0])
        drop_busca_inicio.addItem(itens[1])
        drop_busca_fim = QComboBox()
        drop_busca_fim.addItem(itens[0])
        drop_busca_fim.addItem(itens[1])

        # Create a new QHBoxLayout for the search box layout
        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(QLabel("Search:"))
        hbox_layout.addWidget(QLineEdit())
        hbox_layout.addWidget(QPushButton("Go"))

        busca_layout = QVBoxLayout()
        busca_layout.addWidget(QLabel("Results:"))

        layout_careca = QVBoxLayout(tab_careca)
        layout_careca.addWidget(QLabel("Meci careca"))

        layout_personalizada = QVBoxLayout(tab_personalizada)
        layout_personalizada.addWidget(label)
        layout_personalizada.addWidget(drop_busca_inicio)
        layout_personalizada.addWidget(drop_busca_fim)
        layout_personalizada.addLayout(hbox_layout)
        layout_personalizada.addLayout(busca_layout)
        tab_personalizada.setLayout(layout_personalizada)

        # Set the main window layout to be a QVBoxLayout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)

        # Set the main window as the central widget of your application
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

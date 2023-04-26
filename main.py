import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


def add_mes_items(combo_box):
    combo_box.addItem('Janeiro')
    combo_box.addItem('Fevereiro')
    combo_box.addItem('Março')
    combo_box.addItem('Abril')
    combo_box.addItem('Maio')
    combo_box.addItem('Junho')
    combo_box.addItem('Julho')
    combo_box.addItem('Agosto')
    combo_box.addItem('Setembro')
    combo_box.addItem('Outubro')
    combo_box.addItem('Novembro')
    combo_box.addItem('Dezembro')


def add_ano_items(combo_box):
    combo_box.addItem('2020')
    combo_box.addItem('2021')
    combo_box.addItem('2022')
    combo_box.addItem('2023')


def add_pais_items(combo_box):
    combo_box.addItem('Argentina')
    combo_box.addItem('Brasil')
    combo_box.addItem('Chile')
    combo_box.addItem('Colômbia')
    combo_box.addItem('Equador')
    combo_box.addItem('Peru')
    combo_box.addItem('Paraguai')
    combo_box.addItem('Uruguai')


def search():
    mes_inicio = window.mes_drop1.currentText()
    ano_inicio = window.ano_drop1.currentText()
    mes_fim = window.mes_drop2.currentText()
    ano_fim = window.ano_drop2.currentText()
    pais = window.pais_drop.currentText()
    codigo = window.codigo.text()

    print(f'{mes_inicio}/{ano_inicio} até {mes_fim}/{ano_fim} - {pais} - {codigo}')


# Estilização do pograminha:
box_drop_estilo = """
            QGroupBox {
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 10px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 25px;
                padding: 3px 8px;
            }
        """


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Atualização Dashboards')

        label = QLabel('Busca personalizada:', self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mes_drop1 = QComboBox(self)
        add_mes_items(self.mes_drop1)

        self.mes_drop2 = QComboBox(self)
        add_mes_items(self.mes_drop2)

        self.ano_drop1 = QComboBox(self)
        add_ano_items(self.ano_drop1)

        self.ano_drop2 = QComboBox(self)
        add_ano_items(self.ano_drop2)

        self.pais_drop = QComboBox(self)
        add_pais_items(self.pais_drop)
        
        self.codigo = QLineEdit(self)

        drop_ano_mes_layout1 = QHBoxLayout()
        drop_ano_mes_layout1.addWidget(self.mes_drop1)
        drop_ano_mes_layout1.addWidget(self.ano_drop1)

        drop_ano_mes_layout2 = QHBoxLayout()
        drop_ano_mes_layout2.addWidget(self.mes_drop2)
        drop_ano_mes_layout2.addWidget(self.ano_drop2)

        drop_pais_layout = QHBoxLayout()
        drop_pais_layout.addWidget(self.pais_drop)

        drop_busca_inicio = QGroupBox('Início', self)
        drop_busca_inicio.setStyleSheet(box_drop_estilo)
        drop_busca_inicio_layout = QHBoxLayout()
        drop_busca_inicio_layout.addLayout(drop_ano_mes_layout1)
        drop_busca_inicio.setLayout(drop_busca_inicio_layout)

        drop_busca_fim = QGroupBox('Fim', self)
        drop_busca_fim.setStyleSheet(box_drop_estilo)
        drop_busca_fim_layout = QHBoxLayout()
        drop_busca_fim_layout.addLayout(drop_ano_mes_layout2)
        drop_busca_fim.setLayout(drop_busca_fim_layout)

        drop_escolher_pais = QGroupBox('País', self)
        drop_escolher_pais.setStyleSheet(box_drop_estilo)
        drop_escolher_pais_layout = QHBoxLayout()
        drop_escolher_pais_layout.addLayout(drop_pais_layout)
        drop_escolher_pais.setLayout(drop_escolher_pais_layout)
        drop_escolher_pais.setMinimumWidth(265)

        digitar_codigo = QGroupBox('ID de busca', self)
        digitar_codigo.setStyleSheet(box_drop_estilo)
        digitar_codigo_layout = QHBoxLayout()
        digitar_codigo_layout.addWidget(self.codigo)
        digitar_codigo.setLayout(digitar_codigo_layout)
        digitar_codigo.setMinimumWidth(135)

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(drop_escolher_pais)
        hbox_layout.addWidget(digitar_codigo)

        busca = QPushButton('Baixar', self)
        busca.setFixedSize(100, 30)
        busca.clicked.connect(search)
        busca_layout = QVBoxLayout()
        busca_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        busca_layout.addWidget(busca)

        tabs = QTabWidget(self)
        tab_personalizada = QWidget(self)
        tab_automatica = QWidget(self)
        tabs.addTab(tab_personalizada, 'Personalizada')
        tabs.addTab(tab_automatica, 'Automática')

        layout_personalizada = QVBoxLayout(tabs)
        layout_personalizada.addWidget(label)
        layout_personalizada.addWidget(drop_busca_inicio)
        layout_personalizada.addWidget(drop_busca_fim)
        layout_personalizada.addLayout(hbox_layout)
        layout_personalizada.addLayout(busca_layout)
        tab_personalizada.setLayout(layout_personalizada)

        layout_automatica = QVBoxLayout(tabs)
        layout_automatica.addWidget(QLabel('Em construção...'))
        tab_automatica.setLayout(layout_automatica)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = Window()
    window.show()
    sys.exit(app.exec())

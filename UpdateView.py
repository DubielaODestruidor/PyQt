# main.py
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
import sys


class LoadingThread(QThread):
    progressChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        # simulate loading progress and emit progressChanged signal
        for i in range(101):
            self.progressChanged.emit(i)
            QThread.msleep(10)


class LoadingBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create progress label
        self.progress_label = QLabel('Loading...', self)

        # create close button and set it initially disabled
        self.close_button = QPushButton('Close', self)
        self.close_button.setGeometry(80, 60, 60, 25)
        self.close_button.setEnabled(False)
        self.close_button.clicked.connect(self.close)

        # add progress label and close button to layout
        layout = QVBoxLayout()
        layout.addWidget(self.progress_label)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        # set window properties
        self.setGeometry(300, 300, 220, 100)
        self.setWindowTitle('Loading Bar')

    def set_progress(self, value):
        # enable close button when loading is complete
        if value == 100:
            self.close_button.setEnabled(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # create button to start loading
        self.loading_button = QPushButton('Start Loading', self)
        self.loading_button.clicked.connect(self.start_loading)

        # set window properties
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Loading Bar Example')

        # add loading button to layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.loading_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_loading(self):
        # create and show the loading bar
        self.loading_bar = LoadingBar()
        self.loading_bar.show()

        # create and start the LoadingThread
        self.loading_thread = LoadingThread()
        self.loading_thread.progressChanged.connect(self.loading_bar.set_progress)
        self.loading_thread.finished.connect(self.loading_finished)
        self.loading_thread.start()

    def loading_finished(self):
        # enable close button when loading is complete
        self.loading_bar.close_button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

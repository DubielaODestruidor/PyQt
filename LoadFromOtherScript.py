# main.py
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from Func import LoadingBar


class LoadingThread(QThread):
    progressChanged = pyqtSignal(int)

    def run(self):
        # simulate loading progress and emit progressChanged signal
        for i in range(101):
            self.progressChanged.emit(i)
            QThread.msleep(10)


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
        self.show()

    def start_loading(self):
        # create and show the loading bar
        self.loading_bar = LoadingBar()

        # create and start the LoadingThread
        self.loading_thread = LoadingThread()
        self.loading_thread.progressChanged.connect(self.loading_bar.set_progress)
        self.loading_thread.finished.connect(self.loading_finished)
        self.loading_thread.start()

    def loading_finished(self):
        # enable close button when loading is complete
        self.loading_bar.close_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()

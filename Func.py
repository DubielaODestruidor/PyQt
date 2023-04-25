# loading_bar.py
from PyQt6.QtCore import Qt, QThread
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QPushButton

class LoadingBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create progress bar and label
        self.progress_label = QLabel('Loading...', self)
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 30, 200, 25)

        # create close button and set it initially disabled
        self.close_button = QPushButton('Close', self)
        self.close_button.setGeometry(80, 60, 60, 25)
        self.close_button.setEnabled(False)
        self.close_button.clicked.connect(self.close)

        # set window properties
        self.setGeometry(300, 300, 220, 100)
        self.setWindowTitle('Loading Bar')
        self.show()

    def set_progress(self, value):
        # update progress bar value
        self.progress_bar.setValue(value)
        QApplication.processEvents()  # force GUI update

        # enable close button when loading is complete
        if value == 100:
            self.close_button.setEnabled(True)
def show_loading_bar():
    # create and show the loading bar
    app = QApplication([])
    loading_bar = LoadingBar()

    # simulate loading progress
    for i in range(101):
        loading_bar.set_progress(i)
        QThread.msleep(10)

    # close the loading bar when finished
    loading_bar.close()
    app.quit()

import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar, QHBoxLayout


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.i = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Update every 1 second
        self.timer.timeout.connect(self.updateGUI)
        self.timer.start()

    def initUI(self):
        # Create a progress bar widget
        self.progress = QProgressBar(self)
        self.progress.setGeometry(10, 40, 180, 20)
        self.progress.setMinimum(0)
        self.progress.setMaximum(30)

        # Create a label widget with an animated icon
        self.loading = QLabel(self)
        self.loading.setGeometry(200, 40, 20, 20)
        self.movie = QMovie("./loader.gif")
        self.loading.setMovie(self.movie)
        self.movie.start()

        # Create a label widget for the iteration count
        self.label = QLabel("Iteration: 0", self)
        self.label.setGeometry(10, 10, 150, 30)

        self.setWindowTitle("Looping Function")
        self.setGeometry(100, 100, 240, 80)
        self.show()

    def updateGUI(self):
        self.i += 1
        self.label.setText(f"Iteration: {self.i}")
        self.progress.setValue(self.i)
        if self.i >= 30:
            self.timer.stop()
            self.movie.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())

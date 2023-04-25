from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie, QPainter
from PyQt6.QtWidgets import QApplication, QWidget

class LoadingIcon(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.movie = QMovie("loading.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        frame = self.movie.currentPixmap()
        frame_rect = frame.rect()
        frame_rect.moveCenter(self.rect().center())
        painter.drawPixmap(frame_rect, frame)

if __name__ == '__main__':
    app = QApplication([])
    widget = LoadingIcon()
    widget.resize(200, 200)
    widget.show()
    app.exec()

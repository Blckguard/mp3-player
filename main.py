from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def main():

    app = QApplication([])
    window = QWidget()
    label = QLabel(window)
    button = QPushButton(window)
    layout = QVBoxLayout()


    window.setWindowTitle('Mp3 Player')
    window.setGeometry(0, 0, 450, 450)
    label.setText('Yo what up')
    button.setIcon(QIcon('images/play-button.png'))
    button.setGeometry(200, 370, 50, 50)

    window.setLayout(layout)

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
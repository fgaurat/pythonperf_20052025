from PySide6.QtWidgets import QApplication, QMainWindow
from qt_customer_window import Ui_MainWindow


class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        # self.ui = Ui_MainWindow()
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication()
    window = MainWindow()


    window.show()
    app.exec()

if __name__ == '__main__':
    main()
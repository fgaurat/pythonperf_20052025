from PySide6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from qt_customer_window import Ui_MainWindow
from CustomerDAO import CustomerDAO

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,dao:CustomerDAO):
        # self.ui = Ui_MainWindow()
        super().__init__()
        self.setupUi(self)
        self.__dao = dao
        self.load_data()

    def load_data(self):
        customers = list(self.__dao.findAll())
        nb_rows = len(customers)
        self.customersTable.setRowCount(nb_rows)

        for row_number,customer in enumerate(customers):
            self.customersTable.setItem(row_number,0,QTableWidgetItem(str(customer.id)))
            self.customersTable.setItem(row_number,1,QTableWidgetItem(customer.last_name))
            self.customersTable.setItem(row_number,2,QTableWidgetItem(customer.first_name))
            self.customersTable.setItem(row_number,3,QTableWidgetItem(customer.email))


def main():
    dao = CustomerDAO('customers_db.db')
    # customers = dao.findAll()    
    
    
    app = QApplication()
    window = MainWindow(dao)


    window.show()
    app.exec()

if __name__ == '__main__':
    main()
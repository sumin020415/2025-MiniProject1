import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import cx_Oracle as oci
from contextlib import contextmanager

form_class = uic.loadUiType('./mini_pro1/main.ui')[0]
form_class2 = uic.loadUiType("./mini_pro1/main.ui")[0]
form_class3 = uic.loadUiType("./mini_pro1/delivery.ui")[0]

# DB 접속 정보
username_m = 'c##test'
password_m = '1234'
host_m = 'localhost'
port_m = '1521'
sid_m = 'xe'

def get_connection():
    return oci.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')

@contextmanager
def db_cursor():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

class LoginForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("로그인")
        self.pushButton.clicked.connect(self.login_check)
        self.count = 5

    def login_check(self):
        id = self.lineEdit.text()
        pw = self.lineEdit_2.text()

        with db_cursor() as cursor:
            cursor.execute("SELECT role FROM cmemberlist WHERE user_id = :1 AND user_pw = :2", (id, pw))
            result = cursor.fetchone()

        if result:
            role = result[0]
            if role == 'manager':
                self.open_main()
            elif role == 'delivery':
                self.open_delivery()
            self.close()
        else:
            self.count -= 1
            QMessageBox.critical(self, "오류", f"아이디 또는 비밀번호가 잘못되었습니다. 남은 시도 횟수: {self.count}")
            if self.count == 0:
                QMessageBox.critical(self, "경고", "5회 이상 틀렸습니다. 프로그램을 종료합니다.")
                sys.exit()

    def open_main(self):
        self.main = MainWindow()
        self.main.show()

    def open_delivery(self):
        self.delivery = Delivery()
        self.delivery.show()

class MainWindow(QMainWindow, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("재고관리 프로그램")
        self.searchButton.clicked.connect(self.search_product)
        self.refreshButton.clicked.connect(self.load_products)
        self.load_products()

    def search_product(self):
        search_text = self.searchInput.text()

        with db_cursor() as cursor:
            cursor.execute("SELECT * FROM cproductlist WHERE product_name LIKE '%' || :1 || '%'", (search_text,))
            result = cursor.fetchall()

        self.tableWidget.setRowCount(len(result))
        for row_idx, row_data in enumerate(result):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def load_products(self):
        with db_cursor() as cursor:
            cursor.execute("SELECT * FROM cproductlist")
            result = cursor.fetchall()

        self.tableWidget.setRowCount(len(result))
        for row_idx, row_data in enumerate(result):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

class Delivery(QMainWindow, form_class3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("배송 프로그램")
        self.pushButton.clicked.connect(self.register_delivery)
        self.pushButton_2.clicked.connect(self.load_deliveries)
        self.load_deliveries()

    def register_delivery(self):
        delivery_id = self.lineEdit.text()
        product_id = self.lineEdit_2.text()
        product_name = self.lineEdit_3.text()
        quantity = int(self.lineEdit_4.text())
        delivery_date = self.lineEdit_5.text()

        with db_cursor() as cursor:
            cursor.execute("INSERT INTO cdeliverylist VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))",
                           (delivery_id, product_id, product_name, quantity, delivery_date))

        QMessageBox.information(self, "성공", "배송 등록이 완료되었습니다.")
        self.load_deliveries()

    def load_deliveries(self):
        with db_cursor() as cursor:
            cursor.execute("SELECT * FROM cdeliverylist")
            result = cursor.fetchall()

        self.tableWidget.setRowCount(len(result))
        for row_idx, row_data in enumerate(result):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
import sys

class frmUserPass(QDialog):
    def __init__(self):
        super().__init__()
        self.pool = None
        self.kernel = None
        self.isAdd = False
        self.title = 'Enter Username & Password'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 150
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Username:")
        self.txtUser = QLineEdit()
        self.label2 = QLabel()
        self.label2.setText("Password:")
        self.txtPass = QLineEdit()
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.btnAdd = QPushButton()
        self.btnAdd.setText("OK")
        self.btnAdd.clicked.connect(self.btnAdd_onclick)
        self.btnExit = QPushButton()
        self.btnExit.setText("Cancel")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.txtUser)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.txtPass)
        self.layout.addWidget(self.btnAdd)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.exec_()

    def btnExit_onclick(self):
        self.close()

    def btnAdd_onclick(self):
        self.user   = self.txtUser.text()
        self.passwd = self.txtPass.text()
        self.isAdd  = True
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    frmUserPass()
    sys.exit(app.exec_())
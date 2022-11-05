# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from database import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 368)
        font = QtGui.QFont()
        font.setFamily("RSU")
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AddpushButton = QtWidgets.QPushButton(Form)
        self.AddpushButton.setGeometry(QtCore.QRect(150, 270, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AddpushButton.setFont(font)
        self.AddpushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AddpushButton.setAcceptDrops(False)
        self.AddpushButton.setShortcut("")
        self.AddpushButton.setAutoDefault(False)
        self.AddpushButton.setDefault(False)
        self.AddpushButton.setFlat(False)
        self.AddpushButton.setObjectName("AddpushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.AddpushButton_2 = QtWidgets.QPushButton(Form)
        self.AddpushButton_2.setGeometry(QtCore.QRect(260, 270, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AddpushButton_2.setFont(font)
        self.AddpushButton_2.setObjectName("AddpushButton_2")
        self.idcoffeetext = QtWidgets.QLineEdit(Form)
        self.idcoffeetext.setGeometry(QtCore.QRect(150, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idcoffeetext.setFont(font)
        self.idcoffeetext.setObjectName("idcoffeetext")
        self.menucoffeetext = QtWidgets.QLineEdit(Form)
        self.menucoffeetext.setGeometry(QtCore.QRect(150, 110, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menucoffeetext.setFont(font)
        self.menucoffeetext.setObjectName("menucoffeetext")
        self.descriptiontext = QtWidgets.QLineEdit(Form)
        self.descriptiontext.setGeometry(QtCore.QRect(150, 160, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descriptiontext.setFont(font)
        self.descriptiontext.setObjectName("descriptiontext")
        self.pricetext = QtWidgets.QLineEdit(Form)
        self.pricetext.setGeometry(QtCore.QRect(150, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pricetext.setFont(font)
        self.pricetext.setObjectName("pricetext")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "เพิ่มเมนูกาแฟ"))
        self.AddpushButton.setText(_translate("Form", "ตกลง"))
        self.label_2.setText(_translate("Form", "ID"))
        self.label_3.setText(_translate("Form", "ชื่อเมนู"))
        self.label_4.setText(_translate("Form", "รายละเอียด"))
        self.label_5.setText(_translate("Form", "ราคา"))
        self.AddpushButton_2.setText(_translate("Form", "ยกเลิก"))
        self.AddpushButton.clicked.connect(self.insertDatabase)
    
    def insertDatabase(self):
        ID = self.idcoffeetext.text()
        menu = self.menucoffeetext.text()
        description = self.descriptiontext.text()
        price = self.pricetext.text()
        if (ID == '' or menu == '' or description == '' or price == ''):
            print("Please fill all data")
        else:
            con = pymysql.connect(host="localhost", database="project python",
                                  user=userSQL, password=passSQL, charset="utf8")
            cursor = con.cursor()
            cursor.execute("INSERT INTO coffee (COFFEE_ID, MENU_NAME, MENU_DETAIL, MENU_PRICE) VALUES (%s, %s, %s, %s)",
                           (ID, menu, description, price))
            con.commit()
            self.idcoffeetext.setText("")
            self.menucoffeetext.setText("")
            self.descriptiontext.setText("")
            self.pricetext.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

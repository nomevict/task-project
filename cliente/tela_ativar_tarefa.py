from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_ativar(object):
    """
    Classe que configura a interface grafica de ativar a tarefa.

    Responsavel por configurar a interface grafica da janela de ativar das tarefas utilizando a biblioteca PyQt5.
    """
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(712, 597)
        Cadastro.setStyleSheet("background-color: rgb(0, 90, 142);")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(240, 60, 241, 21))
        self.label.setObjectName("label")
        self.excluir_tarefa_Button_3 = QtWidgets.QPushButton(Cadastro)
        self.excluir_tarefa_Button_3.setGeometry(QtCore.QRect(370, 540, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.excluir_tarefa_Button_3.setFont(font)
        self.excluir_tarefa_Button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_tarefa_Button_3.setStyleSheet("QPushButton{ color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); border-radius: 10px; } QPushButton:hover{ color: rgb(255, 255, 255); background-color: rgb(0, 0, 0); }")
        self.excluir_tarefa_Button_3.setObjectName("excluir_tarefa_Button_3")
        self.excluir_tarefa_Button = QtWidgets.QPushButton(Cadastro)
        self.excluir_tarefa_Button.setGeometry(QtCore.QRect(220, 540, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.excluir_tarefa_Button.setFont(font)
        self.excluir_tarefa_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_tarefa_Button.setStyleSheet("QPushButton{ color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); border-radius: 10px; } QPushButton:hover{ color: rgb(255, 255, 255); background-color: rgb(0, 0, 0); }")
        self.excluir_tarefa_Button.setObjectName("excluir_tarefa_Button")
        self.excluir_tarefa_Button_2 = QtWidgets.QPushButton(Cadastro)
        self.excluir_tarefa_Button_2.setGeometry(QtCore.QRect(600, 560, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.excluir_tarefa_Button_2.setFont(font)
        self.excluir_tarefa_Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_tarefa_Button_2.setStyleSheet("QPushButton{ color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); border-radius: 10px; } QPushButton:hover{ color: rgb(255, 255, 255); background-color: rgb(0, 0, 0); }")
        self.excluir_tarefa_Button_2.setObjectName("excluir_tarefa_Button_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(Cadastro)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 140, 631, 371))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")  # Add this line
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        # Set the width of the "Description" column to 300 pixels (adjust the width as needed)
        self.tableWidget_2.setColumnWidth(2, 329)

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Tasks</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.excluir_tarefa_Button_3.setText(_translate("Cadastro", "Excluir"))
        self.excluir_tarefa_Button.setText(_translate("Cadastro", "Ativar"))
        self.excluir_tarefa_Button_2.setText(_translate("Cadastro", "Voltar"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Cadastro", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Cadastro", "Titulo"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Cadastro", "Descricao"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Cadastro", "Prazo"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_ativar()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())

from PyQt5 import uic,QtWidgets

def listar_dados():
    dado = lista.lineEdit.text() #type: ignore
    lista.listWidget.addItem(dado) #type: ignore
    lista.lineEdit.setText('')#type: ignore
        
def deletar():
    lista.listWidget.clear() #type: ignore
    
app=QtWidgets.QApplication([])

lista=uic.loadUi('lista.ui')
lista.pushButton.clicked.connect(listar_dados) #type: ignore
lista.pushButton_2.clicked.connect(deletar)#type: ignore

lista.show() #type: ignore
app.exec_()
from conta import Conta
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
        
    def abre_conta(self, conta):
        self.contas.append(["CONTA:", conta])
        
    def lista_conta(self):
        for c in self.contas:
            print(c)
            
    
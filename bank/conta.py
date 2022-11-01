

class Conta:
    def __init__(self, cliente, numero, saldo=0):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []

    def resumo(self):
        print(
            f'Nome: {self.cliente.nome}, Tel: {self.cliente.telefone} \nCC Numero: {self.numero} Saldo: {self.saldo: 10.2f}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print('\nSaldo indisponivel\n')

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:8.2f}')
        print(f'\nSALDO R$: {self.saldo:8.2f}')
        
class ContaEspecial(Conta):
    def __init__(self, cliente, numero, saldo=0, limite=0):
        super().__init__(cliente, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])

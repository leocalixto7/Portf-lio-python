from cliente import Cliente
from conta import Conta, ContaEspecial

if __name__ == '__main__':
    
    leo = Cliente('Leonardo', '777-1000')
    
    c1 = ContaEspecial(leo, leo, 100, 1000)
    
    c1.saque(190) 
    c1.deposito(30)
    
    print(c1.resumo())
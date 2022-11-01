from cliente import Cliente
from conta import Conta
from banco import Banco

if __name__ == '__main__':
    
    c1 = Cliente("Leo", "4444-5555")
    c2 = Cliente("Vitoria", "7777-1313")
        
       
#Manipulação de conta--------

    cc1 = Conta(c1, '777-1', 1000)
    cc2 = Conta(c2, '999-1', 2000 )
    
    cc1.saque(100)
    cc1.saque(500)
    cc1.deposito(5000)
    print(cc1.resumo())
    
#MANIPULAÇÃO BANCO------------

    tatu = Banco('tatu')
    
    tatu.abre_conta(cc1.numero)
    tatu.abre_conta(cc2.numero)
    
    #print(tatu.lista_conta())
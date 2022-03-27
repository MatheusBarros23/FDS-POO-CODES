#Vamos usar o mesmo exemplo com as contas

class Conta:
    nomeCliente = "Nome"; 
    __saldo = 13451.78; # com "__" vamos privatizar uma variavel

conta1 = Conta();
conta1.nomeCliente="Matheus" #Até aqui tudo certo, 

print(conta1.nomeCliente)
print(conta1.__saldo)
class Conta:
    nomeCliente = "Nome"; 
    __saldo = 13451.78; # com "__" vamos privatizar uma variavel
    def getSaldo(self): #Precisamos colocar o self como parametro pois ele faz referencia a uma variavel interna
        return self.__saldo #aqui retornamos o valor atribuido a variavel __saldo
    def mudarSaldo(self,valor): 
        self.__saldo = valor 

conta1 = Conta();
conta1.nomeCliente="Matheus"
conta1.mudarSaldo(3000000)

print(conta1.nomeCliente)
print(f"Seu saldo é de: R${conta1.getSaldo():.2f}") #Assim, utilizando um método do mesmo objeto, conseguimos acessar a variavel privada
    
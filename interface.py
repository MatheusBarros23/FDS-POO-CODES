from abc import ABCMeta, abstractmethod

class Funcionario(metaclass=ABCMeta): #Aqui estamos referenciando ABCMeta para que a classe Funcionario seja considerada uma MetaClass e possa receber o @abstractmethod.
                            # De modo a criar um "método abstrato" como forma de reproduzir uma interface. 
    nome=""
    id=0
    
    @abstractmethod #Deste modo, ira marcar este método como abstrato
    def validarLogin (self,login,senha):
        pass

class Diretor(Funcionario):
    def fecharContrato(self):
            print("Contrato Fechado")
    def cancelarContrato(self):
        print("Contrato Cancelado")
    def validarLogin (self,login,senha):
        print(f"O login do Diretor: {login} foi realizado")

class Gerente(Funcionario):
    def realizarContrato(self):
        print("Contrato Realizado")
    def validarLogin (self,login,senha):
        print(f"O login do Gerente: {login} foi realizado")
#diretor
d1=Diretor()
d1.nome="Matheus"
d1.id=123
d1.fecharContrato()
d1.validarLogin("Matheus.Barros",123)

#gerente
g1=Gerente()
g1.nome="Kryno"
g1.id=567
g1.realizarContrato()
g1.validarLogin("Kryno.BK",909)
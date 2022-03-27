class Humano:
    def falar(self,falado):
        print(f"Falar: {falado}")
    def gritar(self,gritado):
        print(f"GRITAR: {gritado}")
    def comer(self):
        print("Humano comendo...\n")

class Cachorro:
    def latido(self):
        print("Latiu: AU!")
    def rosna(self):
        print("Rosnou: rrrrrrr!")
    def comer(self):
        print("Cachorro comendo...")
#humano        
pessoa = Humano()
pessoa.falar("Olá")
pessoa.gritar("ARROZ!")
pessoa.comer()
#cachorro        
rex = Cachorro()
rex.rosna()
rex.latido()
rex.comer()

#Apesar de ambos terem um método com o mesmo nome, ele não é compartilhado entre as classes!
    #É um "comportamento" diferente entre as classes.
#Cada tipo de Classe possuem seus proprios métodos!
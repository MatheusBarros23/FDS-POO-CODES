class Mamiferos(): #classe-mae
    nome = ""
    corPelos=""
    def comer(self):
        print("Comendo...")

class Cachorro(Mamiferos): #Para herdar de uma classe, precisamos referenciar no parametro qual classe-mãe que será herdada pela filha 
    def latir(self):
        print("AUUUU!")

class Humano(Mamiferos): #classe-filha Humano que herda da classe-mae Mamiferos
    def falar(self,frase):
        print(f"\nHumano falou: {frase}")

rex = Cachorro()
rex.nome="Rex"
rex.corPelos="Laranja"
rex.latir()
rex.comer()

pessoa = Humano()
pessoa.nome="Matheus"
pessoa.corPelos="Pretos"
pessoa.falar("Estou com fomeee ")
pessoa.comer() 
#Logo, vimos que mesmo que não esteja previsto na criação das classes-filhas, ambas herdaram o método .comer() e o atributo corPelos da classe-mãe!
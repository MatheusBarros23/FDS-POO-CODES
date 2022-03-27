class Mamiferos(): #classe-mae
    nome = ""
    corPelos=""

class Cachorro(Mamiferos): #Em Python, para herdar de uma classe-mãe, precisamos referenciar no parâmetro qual classe-mãe que será herdada pela filha
    def latir(self):
        print("AUUUU!")

class Humano(Mamiferos): #classe-filha Humano que herda da classe-mãe Mamíferos
    def falar(self,frase):
        print(f"Humano falou: {frase}\n")

rex = Cachorro()
rex.nome="Rex" #herdado pela classe-mãe Mamiferos
rex.corPelos="Laranja" #herdado pela classe-mãe Mamiferos

pessoa = Humano()
pessoa.nome="Matheus" #herdado pela classe-mãe Mamiferos
pessoa.corPelos="Pretos" #herdado pela classe-mãe Mamiferos

print(pessoa.nome)
print(pessoa.corPelos)
print(pessoa.falar("Olá, bom dia!"))

print(rex.nome)
print(rex.corPelos)
print(rex.latir())
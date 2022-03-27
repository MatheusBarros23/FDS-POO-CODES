class Pessoa():
    #atributos
    nome=""
    idade=0
    #métodos
    def falar(self,frase):
        print(f"{self.nome}, {self.idade} anos, disse: " + frase);


class Aluno (Pessoa):
    def estudar(self,disciplina):
        print(f"{self.nome}, {self.idade} anos, estuda: " + disciplina);


class Professor (Pessoa):
    def ensinar(self,disciplina):
        print(f"{self.nome}, {self.idade} anos, ensina: " + disciplina);
    
    def falar(self,frase): #Sobrescrita com falar() de pessoa
        print(f"{self.nome}, {self.idade} anos, FALA ALTO: " + frase);
    
    def falar(self,frase, quantidade): #Sobrecarga de método com o falar() desta mesma classe! Era pra funcionar os 2! mas o java é limitado e não permite
        print(f"{self.nome}, {self.idade} anos, FALA {quantidade} VEZES ALTO: " + frase);
    

pessoa1 = Professor(); #aqui estou criando - ou instanciando- um objeto!
pessoa1.nome='Matheus'
pessoa1.idade= 27

 #já criado
pessoa1.falar('Olá Bom Dia!'); #já posso executar! -Realizar alguma ação! ()
pessoa1.ensinar('Informática');

#aluno
pessoa2=Aluno();
pessoa2.nome="Kryno"
pessoa2.idade=13

pessoa2.falar("Bom dia, professor!")
pessoa2.estudar("Informática")
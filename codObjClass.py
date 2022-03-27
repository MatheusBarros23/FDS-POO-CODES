#Exemplo de uma classe, da criação de um objeto e atributos.

class Conta: #Aqui criamos uma classe Conta que possui 2 atributos (nomeCliente e o saldo da conta)
    nomeCliente = "Nome"; #Conta1 possui um atributo nomeCliente que é to tipo String 
    saldo = 0.0; # E possui outro atributo saldo que é do tipo float

#conta1
conta1 = Conta(); #Criamos um objeto "conta1", que pertence a classe "Conta" e, por isso, goza de seus atributos/métodos! 
    # Assim, chamamos o conta1.nomeCliente para informar o nome do cliente e posteriormente o saldo, para informar o valor depositado quando da abertura da conta. 
        # (Caso não fosse, sertia atirbuido o valor de 0.0, por padrao)
conta1.nomeCliente="Matheus" 
conta1.saldo=350.30

#conta2
conta2=Conta()
conta2.nomeCliente="Marcos" 
conta2.saldo #propositalmente não foi atribuido valor para provar que 0.0 seria o padrao.

print(conta1.nomeCliente)
print(f"Seu saldo é de: R${conta1.saldo:.2f}")

print("\n"+conta2.nomeCliente)
print(f"Seu saldo é de: R${conta2.saldo:.2f}")
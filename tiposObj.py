class Humano:
    qtdDedos=5

class Ave:
    corAsas="branca"

#humano        
pessoa1 = Humano
print(pessoa1.qtdDedos) #Seria printado o valor 5
print(pessoa1.corAsas) # Somos infomados do erro: "AttributeError: type object 'Humano' has no attribute 'corAsas'"

#ave        
beijaFlor = Ave
print(beijaFlor.corAsas) #seria printado "branca"
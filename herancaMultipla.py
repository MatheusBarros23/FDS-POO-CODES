class ItemLoja:
    codItem =""

class SapatoLoja(ItemLoja): 
    marcaSapato=""
    def nfSapato(self):
        print("Nota Fiscal Sapato: Gerada")

class BoneLoja(ItemLoja): 
    marcaBone=""
    def nfBone(self):
        print("Nota Fiscal Boné: Gerada")

class PromoLoja(BoneLoja,SapatoLoja): #De mesma forma, para que herde de diferentes classes, é preciso que 2 ou mais classes estejam referenciados como parametro na criação da Classe.
    codItem1= SapatoLoja.codItem
    codItem2= BoneLoja.codItem

    def promoCompra(self):
        print(f"Parabens! Você comprou os itens {self.codItem1} e {self.codItem2} na promoção!!")

#sapato
sapJordan1=SapatoLoja()
sapJordan1.codItem=123 #atribuindo o codigo do item na loja herdado de ItemLoja  
sapJordan1.marcaSapato="Nike" #atribuindo valor ao atributo marca da propria classe SapatoLoja     

#bone
boneTotal90=BoneLoja()
boneTotal90.codItem=456 #atribuindo o codigo do item na loja herdado de ItemLoja  
boneTotal90.marcaBone="Nike" #atribuindo valor ao atributo marca da propria classe BoneLoja   

#criando o objeto promoSapBoneNike de Classe PromoLoja, que irá reunir em promoção um boné e um sapato da Nike
promoSapBoneNike = PromoLoja()

#Colocando os dados do Objeto sapJordan1 no novo objeto promoSapBoneNike e, por este, acessando o método nfSapato() da classe herdada
promoSapBoneNike.codItem1=sapJordan1.codItem #atribuindo o codigo do objeto sapJordan1 na promoção promoSapBoneNike
promoSapBoneNike.nfSapato() #metodo nfSapato herdado da Classe SapatoLoja

#Colocando os dados do Objeto boneTotal90 no novo objeto promoSapBoneNike e, por este, acesso o método nfBone() da classe herdada 
promoSapBoneNike.codItem2=boneTotal90.codItem #atribuindo o codigo do objeto boneTotal90 na promoção promoSapBoneNike, que foi herdado de ItemLoja
promoSapBoneNike.nfBone() #metodo nfBone herdado da Classe BoneLoja

#por fim, gerar a compra
promoSapBoneNike.promoCompra()


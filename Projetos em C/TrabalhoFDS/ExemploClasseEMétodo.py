class Fruta:
#o nome da classe

    def __init__(self,tipo,cor):
        self.tipo = tipo
        self.cor = cor



    def frase(self):
        print("minha " + self.tipo + " é da cor " + self.cor)
#definindo dois métodos para a minha classe
#passando o parâmetro "self" de um método para o outro 
#é possivel acessar informações do método "init" pro método "frase"


melancia = Fruta("melancia","verde")
blueberry = Fruta("blueberry","azul escuro")

melancia.frase()
#"ativando" o método


    

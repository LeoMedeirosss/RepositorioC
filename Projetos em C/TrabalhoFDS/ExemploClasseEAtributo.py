class Fruta:
#o nome da classe
    def __init__(self):
        self.tipo = "abacaxi"
        self.cor = "amarelo"
#definindo os atributos da classe


minhafruta = Fruta()
minhafruta.cor = "roxo"
minhafruta.tipo = "uva"

#é possivel também mudar os atributos de maneira simples

print(minhafruta.tipo)
print(minhafruta.cor)
#printando os dois atributos da minha classe
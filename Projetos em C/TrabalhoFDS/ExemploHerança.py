#Definindo a SuperClasse
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("falando")

#subclasse "Aluno" herdando a classe "Pessoa"
class Aluno(Pessoa):
    pass


#subclasse "Seilá" herdando a classe "Pessoa"
class Seilá(Pessoa):
    pass


s1 = Seilá('Leonardo',18)
print(s1.idade)


a1 = Aluno('André',19)
print(a1.nome)
a1.falar()

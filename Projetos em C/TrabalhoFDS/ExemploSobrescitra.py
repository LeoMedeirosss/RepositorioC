class animal:
    def comer(self):
        print("este animal está comendo")
#uma classe com um método que printa uma frase


class coelho(animal):
    def comer(self):
        print("este coelho está tomando sopa de cenoura")


    def comer(self):
        print("este coelho está comendo uma cenoura")
#outra frase com o mesmo método que printa uma frase diferente, já que foi inicializada posteriormente


Coelho = coelho()
Coelho.comer()
#a frase que foi printada foi "este coleho está comendo uma cenoura"




class N:
#o nome da classe

    def __init__(self,num):
#defini uma variavel privada
        self.um = 1
        self._dois = 2
        self.__tres = 3
    def public(self):
        self.__tres;
        print("3")



numero = N('num')
print(numero.um)
print(numero._dois)
#quando tento printar a variavel privada dentro da sua classe, o programa roda
numero.public()

#quando tento printar a variavel privada fora da sua classe, o programa da erro
print(numero.__tres)

        
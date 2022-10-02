class AnimalTerrestre:
    def andar(self):
        print("andando")



class AnimalAquatico:
    def nadar(self):
        print("nadando")

#subclasse herdando as classes "AnimalTerrestre" e "AnimalAquatico"
class Jacaré(AnimalTerrestre, AnimalAquatico):
    pass


J = Jacaré()

J.andar()
J.nadar()

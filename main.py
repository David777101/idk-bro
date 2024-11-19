class Animal:
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour

    def make_noise(self):
        print("Animal made a noise")

class Orcawhale(Animal):
    #Overriding
    def make_noise(self):
        print("OOOOO!")

    def swim(self):
        print("Orca is swimming!")

cat = Animal('Bob', 'Black')



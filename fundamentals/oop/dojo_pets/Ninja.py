from Pet import Pet, Cat

class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.name = first_name + ' ' + last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, pet):
        pet.play()
        return self


    def feed(self, pet):
        pet.eat()
        return self

    def bathe(self, pet):
        pet.noise()
        return self



myDog = Pet('GOGO', 'domestic', 'none')
myCat = Cat('Ieon', 'domestic', 'none')
Me = Ninja('William', 'Liu', 'Candy', 'None', 'a dog and a cat')
Me.feed(myDog).walk(myDog).bathe(myDog)
#health=115, Woof!, energy=105
print('my dog', myDog.health, myDog.energy)

Me.feed(myCat).walk(myCat).bathe(myCat)
#health=110, Meow!, energy=90
print('my cat', myCat.health, myCat.energy)


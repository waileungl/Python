class Pet:
    def __init__(self, name, type, tricks, health = 100, energy = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Woof!")
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks, health = 80, energy = 80):
        super().__init__(name, type, tricks, health, energy)

    def eat(self):
        self.energy += 10
        self.health += 20
        return self

    def play(self):
        self.health += 10
        return self

    def noise(self):
        print('Meow!')

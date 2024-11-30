import random

class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        return f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}'

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you 0_0")
        else:
            print("Sorry, I'm peaceful :)")

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.choice([1, 2, 3, 4])} for you")

class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed / 2)

class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = "Click-click-click"

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
print(db.get_cords())
db.dive_in(6)
print(db.get_cords())

db.lay_eggs()
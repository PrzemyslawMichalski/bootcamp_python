class Animal:

    def __init__(self, name):
        self.name = name
        self.energy = 100

        @property
        def is_alive(self):
            return self.energy > 0

        def move(self, distance):
            self.energy -= 0.1 * distance
            if self.is_alive:
                return distance
            return self.is_alive

        def eat(self, calories):
            self.energy += 0.2 * calories


a = Animal('Zenek')
print(a.move(50))
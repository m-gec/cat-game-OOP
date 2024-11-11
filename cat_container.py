class cat:
    def __init__(self, given_name, given_color):
        self.name = given_name
        self.color = given_color
        self.intelligence = 1
        self.energy = 10
        self.weight = 25

    def train(self):
        self.intelligence += 1
        self.energy -= 1
        self.weight -= 1

    def feed(self):
        self.energy += 1
        self.weight += 1
    
    def sleep(self):
        self.energy -= 1
        self.weight += 1

    def spill(self):
        print(f"name: {self.name}")
        print(f"color: {self.color}")
        print(f"energy: {self.energy}")
        print(f"weight: {self.weight}")
        print(f"intelligence: {self.intelligence}")

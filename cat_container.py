class cat:
    def __init__(self, given_name, given_color):
        self.name = given_name
        self.color = given_color
        self.age = 1
        self.energy = 10
        self.weight = 25
        self.experience = 0

    def train(self):
        self.age += 1
        self.energy -= 1
        self.weight -= 1
        self.experience += 1

    def feed(self):
        self.age += 1
        self.energy += 1
        self.weight += 1

    def spill(self):
        print(f"name: {self.name}", "\n\n", f"color: {self.color}", "\n", f"age: {self.age}", "\n", f"energy: {self.energy}", "\n", f"weight: {self.weight}", "\n", f"experience: {self.experience}", "\n")

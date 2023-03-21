class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def bark(self):
        print(f"{self.name} says WOOF!")
    
    
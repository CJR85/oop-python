class Cat:
    def __init__(self, name):
        self.name = name
        print("Inside Cat init")
    
    def meow(self):
        print(f"{self.name} meows!!!")

class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!!!")

class Lion(Cat):
    def __init__(self, name, pride_name):
        print("Inside Lion init")
        super().__init__(name)
        self.pride_name = pride_name
    def roar(self):
        print(f"{self.name} roars!!!")

# Lion
#     - roar
# Cougar
#     - purr

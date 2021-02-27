
class Shoe:
    def __init__(self, name, mileage=0):
        self.name = name
        self.mileage = mileage

    def print_info(self):
        print(f"Shoe {self.name} has {self.mileage} kilometers.")
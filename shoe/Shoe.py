
class Shoe:
    def __init__(self, name):
        self.name = name
        self.mileage = 0
        self.runs = 0
        self.max_mileage = False

    def print_info(self):
        print(f"INFO: -- {self.name} --")
        print(f"- {self.mileage} total kilometers")
        print(f"- {self.runs} total runs")
        if self.max_mileage:
            print(f"- {self.max_mileage - self.mileage} kilometers left before replacement")

    def add_mileage(self, distance):
        self.mileage += distance
        self.runs += 1

    def set_max_mileage(self, mileage):
        self.max_mileage = float(mileage)

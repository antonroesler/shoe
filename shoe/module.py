import pickle
import os

FULL_PATH = os.getcwd()
DATA_PATH = os.path.join(FULL_PATH, "data")
UNIT = "km"


def save_shoe(name, mileage):
    with open(os.path.join(DATA_PATH, name), "wb+") as file:
        pickle.dump(mileage, file)


def load_shoe(name):
    with open(os.path.join(DATA_PATH, name), "rb+") as file:
        return pickle.load(file)


def unit():
    global UNIT
    if UNIT == "km":
        UNIT = "miles"
    else:
        UNIT = "km"


def add(args):
    name = args[0]
    x = float(load_shoe(name))
    x += float(args[1])
    save_shoe(name, x)


def create(args):
    save_shoe(args[0], 0)


def info(args):
    name = args[0]
    x = load_shoe(name)
    print(f"{name} has {x} km.")

f = {"add": add, "unit": unit, "create": create, "info": info}
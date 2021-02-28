import pickle
import os
from os.path import expanduser

from .Shoe import Shoe

HOME = expanduser("~")
DATA_PATH = os.path.join(HOME, "/Library/Caches/shoe/")
UNIT = "km"


def create_data_dir():
    """Creates the data/ directory."""
    os.mkdir(DATA_PATH)


def save_shoe(name, shoe):
    try:
        with open(os.path.join(DATA_PATH, name), "wb+") as file:
            pickle.dump(shoe, file)
    except FileNotFoundError:
        # Only necessary for the first shoe after a fresh installation.
        create_data_dir()
        save_shoe(name, shoe)


def load_shoe(name):
    with open(os.path.join(DATA_PATH, name), "rb+") as file:
        return pickle.load(file)


def add(args):
    name = args[0]
    shoe = load_shoe(name)
    shoe.add_mileage(float(args[1]))
    save_shoe(name, shoe)


def create(args):
    """To create a shoe args needs to be a list with the shoe's name at index 0."""
    save_shoe(args[0], Shoe(args[0]))


def info(args):
    name = args[0]
    x = load_shoe(name)
    x.print_info()


def set_max_mileage(args):
    name = args[0]
    shoe = load_shoe(name)
    shoe.set_max_mileage(args[1])
    save_shoe(name, shoe)


functions = {"add": add, "create": create, "info": info, "max": set_max_mileage}

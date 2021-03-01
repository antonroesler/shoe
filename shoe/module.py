import pickle
import os
from os.path import expanduser

from .Shoe import Shoe

HOME = expanduser("~")
DATA_PATH = os.path.join(HOME, "/Library/Caches/shoe/")
UNIT = "km"


def create_data_dir():
    """Creates the data/ directory in the user's file system."""
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
    try:
        with open(os.path.join(DATA_PATH, name), "rb+") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


def add(args):
    name = args[0]
    shoe = load_shoe(name)
    if shoe:
        shoe.add_mileage(float(args[1]))
        save_shoe(name, shoe)
    else:
        dont_exist_msg(name)


def dont_exist_msg(name):
    print(f"{name} does not exist. [use 'create {name}' to create a new shoe]")


def create(args):
    """To create a shoe args needs to be a list with the shoe's name at index 0."""
    save_shoe(args[0], Shoe(args[0]))


def info(args):
    """Prints the shoe's infos."""
    name = args[0]
    shoe = load_shoe(name)
    if shoe:
        shoe.print_info()
    else:
        dont_exist_msg(name)


def set_max_mileage(args):
    """Sets the shoe's maximum mileage to the parameter at args[1]"""
    name = args[0]
    shoe = load_shoe(name)
    if shoe:
        shoe.set_max_mileage(args[1])
        save_shoe(name, shoe)
    else:
        dont_exist_msg(name)


def list_all_shoes():
    """Lists all shoes."""
    for name in os.listdir(DATA_PATH):
        print(name)


def remove_shoe(args):
    """Deletes a shoe."""
    name = args[0]
    try:
        os.remove(os.path.join(DATA_PATH, name))
        print(f"{name} deleted")
    except FileNotFoundError:
        print("0 shoes deleted")


functions = {
    "add": add,
    "create": create,
    "info": info,
    "max": set_max_mileage,
    "list": list_all_shoes,
    "ls": list_all_shoes,
    "rm": remove_shoe
}

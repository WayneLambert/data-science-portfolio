import random as r

class Pound:
    value = 1.00
    colour = "gold"
    num_edges = 12
    diameter = 23.03        # in mm
    thickness = 2.8         # in mm
    heads = True
    mass = 8.75             # in g
    materials = ["nickel", "brass"]
    designer = "Jody Clark"
    release_date = 31/10/2016

coin1 = Pound()
print(type(coin1))
print(coin1.value)


# The below is a constructor method
# self is a chosen keyword that represents an initialised instance of the class.
# Self can be any keyword, however the convention is to use "self"
def __init__(self, rare = False):
    self.rare = rare
    self.value = 1.25 if self.rare else 1.00
    self.colour = "greenish"
    self.num_edges = 12
    self.diameter = 23.03


# The below is a custom method function that turns the coin greenish when it rusts
def rust(self):
    self.colour = "greenish"


def clean(self):
    self.colour = "gold"


def flip(self):
    coin_toss_options = [True, False]
    choice = r.choice(coin_toss_options)
    self.heads = choice


def __del__(self):
    print("Coin Spent!")


del coin1   # This calls the destructor method for the coin1 object

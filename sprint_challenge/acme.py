
from random import randint

class Product():
    """As an employee of Acme Corporation, you're always looking for ways to better
    organize the vast quantities and variety of goods your company manages and
    sells
    Params:
    - `name` (string with no default)
    - `price` (integer with default value 10)
    - `weight` (integer with default value 20)
    - `flammability` (float with default value 0.5)
    - `identifier` (integer, automatically genererated as a random (uniform) number
      anywhere from 1000000 to 9999999, includisve)(inclusive).
    return:
    """

    def __init__(self, name, identifier=randint(1000000,10000000), price=10, weight=20, flammability=0.5):
        #supe Product, self).__init__()
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier




#if __name__ =="__main__":

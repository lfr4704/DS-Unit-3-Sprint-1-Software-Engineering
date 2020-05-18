
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

    def stealability(self):
        """
        calculates the price divided by the weight, and then returns a message: if the ratio
        is less than 0.5 return "Not so stealable...", if it is greater or equal to 0.5 but
        less than 1.0 return "Kinda stealable.", and otherwise return "Very stealable!"
        """
        price_weight_ratio = self.price/self.weight
        if price_weight_ratio < 0.5:
            return "Not so stealable ..."
        elif price_weight_ratio >= 0.5 and price_weight_ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable"

    def explode(self):
        """
        Calculates the flammability times the weight, and then returns a message: if the product
        is less than 10 return "...fizzle.", if it is greater or equal to 10 but less than 50
        return "...boom!", and otherwise return "...BABOOM!!"
        """

        explosion_power = self.flammability * self.weight
        if explosion_power < 10:
            return "fizzle"
        elif explosion_power >= 10 and explosion_power < 50:
            return "...bom!"
        else:
            return "...BABOOM!!"





#if __name__ =="__main__":

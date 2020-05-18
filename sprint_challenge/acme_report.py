from random import randint, sample, uniform, randrange
from acme import Product
import pandas as pd

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    should generate a given number of products (default
      30), randomly, and return them as a list
    """
    products = []
    # TODO - your code! Generate and add random products.
    for x in range(num_products):
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0, 2.5)
        name = f'{ADJECTIVES[randrange(len(ADJECTIVES))]} {NOUNS[randrange(len(NOUNS))]}'
        products.append(Product(name, price, weight, flammability))

    return products


def inventory_report(products):
    """
    takes a list of products, and prints a "nice" summary
    """
    # TODO - your code! Loop over the products to calculate the report.
    df = pd.Series(products)
    print(df)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')




if __name__ == '__main__':
    #inventory_report(generate_products())
    inventory_report(generate_products())

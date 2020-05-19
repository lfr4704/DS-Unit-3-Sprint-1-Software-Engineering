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
        products.append(Product(
        name = f'{ADJECTIVES[randrange(len(ADJECTIVES))]} {NOUNS[randrange(len(NOUNS))]}',
        price = randint(5, 100),
        weight = randint(5, 100),
        flammability = uniform(0.0, 2.5)))
    return products


def inventory_report(products):
    """
    takes a list of products, and prints a "nice" summary
    """
    # TODO - your code! Loop over the products to calculate the report.
    names = set() # what are sets: https://realpython.com/python-sets/
    total_price =0
    total_weight=0
    total_flammability=0.0
    for product in products:
        names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names:{len(names)}')
    print(f'Average price: {total_price/len(products)}')
    print(f'Average weight: {total_weight/len(products)}')
    print(f'Average flammability:{total_flammability/len(products)}')


if __name__ == '__main__':
    #inventory_report(generate_products())
    inventory_report(generate_products())

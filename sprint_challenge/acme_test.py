import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """Test defaul weight is 20"""
        prod = Product('cool product')
        self.assertEqual(prod.weight, 20)

    def test_explosion_power(self):
        prod = Product('very explosive', weight=20, flammability=10)
        self.assertEqual(prod.explode(), '...BABOOM!!')

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme Report works"""
    def test_default_products(self):
        """test that defuaul is 30"""
        self.assertEqual(len(generate_products()),30)

    def test_nouns_adjectives(self):
        """check that products have all valid possible names"""
        for product in generate_products:
            adjective, noun = product.name.split()
            self.assertEqual(adjective, ADJECTIVES)
            self.assertEqual(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()

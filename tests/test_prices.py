import unittest
from src.prices import Prices

class TestPrices(unittest.TestCase):

    def setUp(self):
        self.prices = Prices()

    def test_set_price(self):
        self.prices.set_price('test')
        self.assertEqual(self.prices.prices['test'], 20)

    def test_get_movie_counts(self):
        items = ['input :', 'Back to the Future 1', 'Back to the Future 2', 'Back to the Future 2', 'Other Movie', 'Back to the Future 1']
        counts = self.prices.get_movie_counts(items)
        self.assertEqual(counts['back to the future 1'], 2)
        self.assertEqual(counts['back to the future 2'], 2)
        self.assertEqual(counts['other movie'], 1)

    def test_get_total(self):
        counts = {'back to the future 1': 2, 'back to the future 2': 2, 'other movie': 1}
        total_fttp, total_others = self.prices.get_total(counts)
        self.assertEqual(total_fttp, 60)
        self.assertEqual(total_others, 20)

    def test_get_discount(self):
        counts = {'back to the future 1': 1, 'back to the future 2': 1, 'back to the future 3': 1}
        discount = self.prices.get_discount(counts)
        self.assertEqual(discount, 0.2)

        counts = {'back to the future 1': 1, 'back to the future 2': 1}
        discount = self.prices.get_discount(counts)
        self.assertEqual(discount, 0.1)

        counts = {'back to the future 2': 1, 'back to the future 3': 1}
        discount = self.prices.get_discount(counts)
        self.assertEqual(discount, 0.1)

        counts = {'back to the future 1': 1, 'back to the future 3': 1}
        discount = self.prices.get_discount(counts)
        self.assertEqual(discount, 0.1)

        counts = {'back to the future 1': 1, 'other movie': 1}
        discount = self.prices.get_discount(counts)
        self.assertEqual(discount, 0)

if __name__ == '__main__':
    unittest.main()

import unittest
from src.basket import Basket

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()
    
    def test_read_file(self):
        ''' Test that read_file returns the content of a file as a list of lines
        and that we dont have neither NA nor "input" included
        '''
        text_file = 'test_input.txt'
        expected_output = ['input :', '', 'Back to the Future 1', '', 'Back to the Future 2', '', 'Back to the Future 3']
        self.assertEqual(self.basket.read_file(text_file), expected_output)

    
    def test_write_file(self):
        '''
        Test what write_file append a file with the correct output
        '''
        text_file = "test_output.txt"
        cost = 42
        self.basket.write_file(text_file, cost)
        with open(text_file, 'r') as file:
            lines = file.readlines()
            expected_ouput = ['\n', '\n', 'Output : \n', '\n', '42']
            self.assertEqual(lines, expected_ouput)

if __name__ == '__main__':
    unittest.main()

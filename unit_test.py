import unittest
import numpy as np
import main



class Test(unittest.TestCase):

    def setUp(self):
        self.testdata = main.load('src/testData.csv')

    def test_get_color(self):
        self.assertEqual(main.get_color([10]), ['darkgreen'])
        self.assertEqual(main.get_color([110]), ['yellowgreen'])
        self.assertEqual(main.get_color([110,56,345,2234,2323234]), ['yellowgreen', 'lime', 'darkorange', 'maroon', 'maroon'])
        self.assertEqual(main.get_color([0,50,100,150,300,500]), ['darkgreen', 'lime', 'yellowgreen', 'gold', 'darkorange', 'maroon'])
        self.assertEqual(main.get_color([-100]), ['maroon'])
        print('get color test passed')

    def test_load_price(self):

        self.assertEqual(main.load_price(), main.load_price())
        print('load price pass')




if __name__ == '__main__':
    unittest.main()
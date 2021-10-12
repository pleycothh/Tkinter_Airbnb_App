import unittest
import numpy as np
from main import *
import main
import coverage



class Test(unittest.TestCase):

   # def setUp(self):
    #  pass
      #  self.data = pd.read_csv('src/testData.csv')
       # self.testData = self.data[['name','host_name', 'neighbourhood', 'room_type', 'price', 'latitude', 'longitude']]

    def setUp(self):
        self.window = tk.Tk()
        self.test_get_color()

    def tearDown(self):
        if self.window:
            self.window.destroy()
            self.test_get_color()

    def test_get_color(self):
        self.assertEqual(main.get_color([10]), ['darkgreen'])
        self.assertEqual(main.get_color([110]), ['yellowgreen'])
        self.assertEqual(main.get_color([110,56,345,2234,2323234]), ['yellowgreen', 'lime', 'darkorange', 'maroon', 'maroon'])
        self.assertEqual(main.get_color([0,50,100,150,300,500]), ['darkgreen', 'lime', 'yellowgreen', 'gold', 'darkorange', 'maroon'])
        self.assertEqual(main.get_color([-100]), ['maroon'])

    print(coverage.coverage)


if __name__ == '__main__':
    unittest.main()
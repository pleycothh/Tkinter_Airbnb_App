import unittest



class Test(unittest.TestCase):
    def test_add(self):
        result = 10 + 5
        self.assertEqual(result, 15)



if __name__ == '__main__':
    unittest.main()
import unittest
import calc_app

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        input=calc_app.add("")
        self.assertEqual(input, 0) 

    def test_one_num(self):
        input=calc_app.add("1")
        self.assertEqual(input, 1)
    
    def test_addtion(self):
        input=calc_app.add("1,2")
        self.assertEqual(input, 3)
    

if __name__ == '__main__':
    unittest.main()
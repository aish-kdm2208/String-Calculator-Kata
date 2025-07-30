import unittest
import calc_app

class TestCalculator(unittest.TestCase):
    def test_empty_string(self):
        input=calc_app.add("")
        self.assertEqual(input, 0) 

if __name__ == '__main__':
    unittest.main()
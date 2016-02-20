import unittest
import addition

class TestAddition(unittest.TestCase):

    def test_add2(self):
        self.assertEqual(addition.add2(2,3),5)

    def test_add3(self):
        self.assertEqual(addition.add3(1,2,3),6)

if __name__ == '__main__':
    unittest.main()

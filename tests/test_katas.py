import unittest
import katas 


class TestKatas(unittest.TestCase):
    def test_add(self):
        result = katas.add(3, 4)
        self.assertEqual(result, 7)

    def test_multiply(self):
        result = katas.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_power(self):
        result = katas.power(3, 4)
        self.assertEqual(result, 81)

    def test_factorial(self):
        result = katas.factorial(4)
        self.assertEqual(result, 24)

    def test_fibonacci(self):
        result = katas.fibonacci(8)
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()

import unittest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 1)


if __name__ == '__main__':
    unittest.main()

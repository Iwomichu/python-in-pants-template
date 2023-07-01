import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self) -> None:
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

import unittest
from pyguitest import MyFun


class TestMyFun(unittest.TestCase):
    def test_HelloWorld(self):
        self.assertEqual(MyFun(), "Hello World")

    def test_False(self):
        self.assertFalse(False)


if __name__ == "__main__":
    unittest.main()

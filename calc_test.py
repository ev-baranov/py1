import unittest
from calc import Calculator

class TestStep1(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
            
    def testCalc1(self):
        calculator = Calculator()
        self.assertEqual(4, calculator.add(2,2))        

if __name__ == '__main__':
    unittest.main()
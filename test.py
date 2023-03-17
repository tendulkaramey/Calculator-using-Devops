from calculator import *
import unittest


class testfactorial(unittest.TestCase):

    def test_factorialpositive(self):
        self.assertEqual(factorial(3),6,'should be 6')

    def test_factorialnegative(self):
        self.assertNotEqual(factorial(5),6,'should be 120')

class testsquareroot(unittest.TestCase):

    def test_squareroottestpositive(self):
        self.assertEqual(squareroot(4),2,'should be 2')

    def test_squarerootnegative(self):
        self.assertNotEqual(squareroot(64),6,'should be 8')

class testpower(unittest.TestCase):

    def test_powerpositive(self):
        self.assertEqual(power(2,3),8,'should be 8')

    def test_powernegative(self):
        self.assertNotEqual(power(2,2),6,'should be 4')

class testlog(unittest.TestCase):

    def test_logpositive(self):
        self.assertEqual(naturallog(1),0,'should be 0')

    def test_lognegative(self):
        self.assertNotEqual(naturallog(25),2,'should be 3.2188758248682006')


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
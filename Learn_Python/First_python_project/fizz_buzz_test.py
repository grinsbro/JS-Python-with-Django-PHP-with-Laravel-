import firstproject
from firstproject import getreply
import unittest 
from unittest import TestCase
from unittest import main

class FizzBuzzTests(unittest.TestCase):

    def test_fizz(self):
        number = 6

        result = firstproject.getreply(number)

        self.assertEqual(result, 'Fizz')
    
    def test_buzz(self):
        number = 10

        result = firstproject.getreply(number)

        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        number = 15 
        
        result = firstproject.getreply(number)

        self.assertEqual(result, 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()


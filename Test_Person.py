import unittest
from Hero import *


class Tests(unittest.TestCase):

    def setUp(self):
        self.person = Person(10, 10)

    def test_get_mana_test(self):
        print(type(self. person.get_mana()))

if __name__ == '__main__':
    unittest.main()

import unittest

from pokedex import Pokedex

class TestPokedex(unittest.TestCase):
      def setUp(self):
          self.pokedex = Pokedex()


class TestRead(TestPokedex):
      def test_all_pkemons(self):
          self.assertEqual(self.pokedex, 809)

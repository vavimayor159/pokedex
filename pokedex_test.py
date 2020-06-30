import unittest

from pokedex import Pokedex

class TestPokedex(unittest.TestCase):
    def setUp(self):
        self.pokedex = Pokedex()


class TestReadFunction(TestPokedex):
    def test_all_pkemons(self):
        self.assertEqual(len(self.pokedex.pokemonsList), 809)

class TestSearchFunction(TestPokedex):
    def test_search_by_id(self):
        self.pokedex.IDsearch(802)
        self.assertEqual(self.pokedex.PokemonSearched.name, "Marshadow")
        self.assertEqual(self.pokedex.PokemonSearched.id, 802)
        self.assertEqual(self.pokedex.PokemonSearched.type, ["Fighting", "Ghost"] )
        self.assertEqual(self.pokedex.PokemonSearched.base, {"HP": 90,
        "Attack": 125,
        "Defense": 80,
        "Sp. Attack": 90,
        "Sp. Defense": 90,
        "Speed": 125} )



if __name__ == '__main__':
    unittest.main()
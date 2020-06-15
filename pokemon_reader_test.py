import unittest

from pokemon_reader import PokemonReader
from pokemon_reader import Pokemon

class PokemonReaderTest(unittest.TestCase):
    def setUp(self):
        self.pokemon_reader = PokemonReader('pokedex_test.json')


class TestInit(PokemonReaderTest):
    def test_creates_pokemon_reader(self):
        self.assertNotEqual(self.pokemon_reader, None)

class TestRead(PokemonReaderTest):    
    def test_move_data_new_variable(self):
        self.pokemon_reader.readData()
        self.assertNotEqual(self.pokemon_reader.data, None)

    def test_move_data_pokemon_object(self):
        self.assertEqual(self.pokemon_reader.readData()["id"], 802)



class PokemonTest(unittest.TestCase):
    def setUp(self):
        self.pokemons = Pokemon()

class TestPopos(PokemonTest):
    def test_empty_contructor(self):
        self.assertEqual(self.pokemons.name, "")
        self.assertEqual(self.pokemons.id, 0)
        self.assertEqual(self.pokemons.type, "")
        self.assertEqual(self.pokemons.base, "")



if __name__ == '__main__':
    unittest.main()
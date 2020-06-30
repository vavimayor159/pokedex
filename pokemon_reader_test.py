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
        self.pokemon = Pokemon()

class TestPopos(PokemonTest):
    def test_empty_contructor(self):
        self.assertEqual(self.pokemon.name, "")
        self.assertEqual(self.pokemon.id, 0)
        self.assertEqual(self.pokemon.type, "")
        self.assertEqual(self.pokemon.base, "")
    
    def test_value_constructor(self):
        self.pokemon = Pokemon({
            "id": 802,
            "name": {
                    "english": "Marshadow",
                    "japanese": "マーシャドー",
                    "chinese": "玛夏多",
                    "french": "Vémini"
            },
            "type": [
                "Fighting",
                "Ghost"
            ],
            "base": {
                "HP": 90,
                "Attack": 125,
                "Defense": 80,
                "Sp. Attack": 90,
                "Sp. Defense": 90,
                "Speed": 125
            }}
        )
        self.assertEqual(self.pokemon.name, "Marshadow")
        self.assertEqual(self.pokemon.id, 802)
        self.assertEqual(self.pokemon.type, ["Fighting", "Ghost"] )
        self.assertEqual(self.pokemon.base, {"HP": 90,
        "Attack": 125,
        "Defense": 80,
        "Sp. Attack": 90,
        "Sp. Defense": 90,
        "Speed": 125} )





if __name__ == '__main__':
    unittest.main()
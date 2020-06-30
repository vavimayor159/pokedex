import json

class PokemonReader:
    def __init__(self, fileName):
        self.fileName = fileName

        pass

    def readData(self):
        with open(self.fileName, 'r') as myfile:
            self.data = myfile.read()
            return  json.loads(self.data)

class Pokemon:

    def __init__(self, pokemonData = None):
        if (pokemonData != None):
            self.name = pokemonData["name"]["english"]
            self.id   = pokemonData["id"]
            self.type = pokemonData["type"]
            self.base = pokemonData["base"]
        else:
            self.name = ""
            self.id   = 0
            self.type = ""
            self.base = ""
        pass


   

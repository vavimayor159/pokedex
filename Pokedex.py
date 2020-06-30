from pokemon_reader import PokemonReader 
from pokemon_reader import Pokemon

class Pokedex:
    def __init__(self):
        self.pokemonsList = PokemonReader('pokedex.json').readData()
        self.pokemonSearched = []
        #print(self.pokemonsList[801])

        """ for number in range(len(self.pokemonsList)):
            print 
            if self.pokemonsList[number]['id'] == 802:
                print(self.pokemonsList[number])
                break
 """
    def IDsearch(self,id):
        for number in range(len(self.pokemonsList)):
            if self.pokemonsList[number]['id'] == id:
                self.PokemonSearched = Pokemon( self.pokemonsList[number])
                print(self.PokemonSearched.name)

if __name__ == '__main__':
    pokedexOn = Pokedex()
    while True:
        try:
            numero = int(input('Id: '))
            if numero in range(len(pokedexOn.pokemonsList)):
                pokedexOn.IDsearch(numero)
                
            else:
                print('No valido')
        except ValueError:
            print('No valido')





# # We can read a JSON file using:
# import json
#
# # read file
# with open('example.json', 'r') as myfile:
#     data=myfile.read()
#
# # parse file
# obj = json.loads(data)
#
# # show values
# print("usd: " + str(obj['usd']))
# print("eur: " + str(obj['eur']))
# print("gbp: " + str(obj['gbp']))

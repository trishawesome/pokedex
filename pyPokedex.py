import requests, os, subprocess

# save the base URL for the API in a constant variable 
BASE = "https://pokeapi.co/api/v2/"
POKEMON_BASE = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_SPECIES = "https://pokeapi.co/api/v2/pokemon-species/"
EVOLUTION_CHAIN = "https://pokeapi.co/api/v2/evolution-chain/" 
TYPE_INFO = "https://pokeapi.co/api/v2/type/" 

cache = {} 

# relevant program functions
def clearTerm(): 
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)

def pokedex(desired): # gets and displays pokemon information. this is the "core" logic

    if desired not in cache: 
        # grab information about desired pokemon with a "get" command. 
        httpResponse = requests.get(POKEMON_BASE + desired)

        # status codes of interest: 
        # 200 -> Success, 404 -> Not found, 429 -> Too many requests, 500+ -> Server error

        if httpResponse.status_code != 200: 
            # signify there was an error to whoever is calling this function
            return -1 

        else: 
            pokemon_data = httpResponse.json() # grab the Pokemon's information
            species_data = requests.get(pokemon_data["species"]["url"]).json() # species gives us further info 
            evolution_data = requests.get(species_data["evolution_chain"]["url"]).json() 
            cache[desired] = [pokemon_data, species_data, evolution_data] 
    else:
        pokemon_data = cache[desired][0] 
        species_data = cache[desired][1] 
        evolution_data = cache[desired][2] 

    # categorize data as needed, from pokemon_data
    name = pokemon_data["name"].capitalize()
    id = pokemon_data["id"]
    types = ", ".join([t["type"]["name"].capitalize() for t in pokemon_data["types"]])
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]

    # from species_data and evolution_data
    evolves_from = species_data["evolves_from_species"]["name"].capitalize() if species_data["evolves_from_species"] else None

    # display the pokemon's information 
    print("\n•☽────✧˖°˖☆˖°˖✧────☾• \n")

    print(f'Name: {name}')
    print(f'ID: {id}')
    print(f'Type: {types}')

    if evolves_from != None: 
        print(f'Evolves from: {evolves_from}')

    print(f'Height: {height}')
    print(f'Weight: {weight}')

    print("\n•☽────✧˖°˖☆˖°˖✧────☾• \n")

    # program completed safely
    return 0 


# Below is the "main" function: 
def main(): 
    while True: 
        clearTerm() 
        desired = ((input("\nWelcome to pyPokédex! Please insert the name or ID of the pokemon you're looking for: ")).lower()).strip() 

        if pokedex(desired) == -1: 
            # logic for failed pokedex 
            print("\nThere was an error; please ensure you're searching for a valid Pokémon.") 

        while True: 
            # .strip() and .lower() handled cleanly in one line
            user_choice = input("\nWould you like to search again? (y/n) ").strip().lower() 
            
            if user_choice in ("y", "n"): 
                break
            
            print("\nYour input was malformed.")

        if user_choice == "n": 
            break

# run the program logic 
main()     





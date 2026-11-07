import requests, os, subprocess

# save the base URL for the API in a constant variable 
POKEMON_BASE = "https://pokeapi.co/api/v2/pokemon/"

# relevant program functions
def clearTerm(): 
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)

def pokedex(desired): # gets and displays pokemon information. this is the "core" logic

    # grab information about desired pokemon with a "get" command. 
    httpResponse = requests.get(POKEMON_BASE + desired)

    # status codes of interest: 
    # 200 -> Success, 404 -> Not found, 429 -> Too many requests, 500+ -> Server error

    if httpResponse.status_code != 200: 
        # signify there was an error to whoever is calling this function
        return -1 

    else: 
        data = httpResponse.json() # grab the Pokemon's information

        name = data["name"].capitalize()
        id = data["id"]
        types = ", ".join([t["type"]["name"].capitalize() for t in data["types"]])
        height = data["height"]
        weight = data["weight"]


    # display the pokemon's information 
    print("\n•☽────✧˖°˖☆˖°˖✧────☾• \n")

    print(f'Name: {name}')
    print(f'ID: {id}')
    print(f'Type: {types}')
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





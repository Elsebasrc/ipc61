import requests
#Nombre:Brian Sebastian Reyna Castillo
#Matricula: 2127309

def get_pokemons (url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset':offset}if offset else{}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        pauload = response.json()
        results = pauload.get('results',[])

        if results :
            for pokemon in results:
                name= pokemon['name']
                print(name)
        next= input('Continuar listando ? [Y/N]').lower()
        if next == 'y':
            get_pokemons(offset=offset+20)
if __name__ == '__main__':
    url='http://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()
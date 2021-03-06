import requests
import json

hero_list_data = ['Hulk', 'Captain', 'America', 'Thanos']

def get_data(hero_list):
    result_data = {}
    for hero in hero_list:
        result = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero}')
        result_data[result.json()['results'][0]['name']] = result.json()['results'][0]['powerstats']['intelligence']

    return max(result_data.items())

result = get_data(hero_list_data)
print(result)
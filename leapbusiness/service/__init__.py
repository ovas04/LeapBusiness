from array import array
import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from .Scrap_algorithm import Scrap_algorithm


def main():
    print("-------------------------------")
    print("Main")
    update_steamSpy_list()
    update_data()
    return True


def update_steamSpy_list():
    print("-------------------------------")
    print("Updating List")
    url = 'https://steamspy.com/api.php?request=all&page='
    array = []
    count = 0
    status_code = 200

    while(status_code == 200):
        try:
            response = urlopen(url + str(count))
        except HTTPError as error:
            print(error.status, error.reason)
            break
        except URLError as error:
            print(error.reason)
            break
        status_code = response.getcode()
        items = json.loads(response.read())
        for item in items:
            print(item)
            array.append(item)
        count += 1

    print('No response from page ' + str(count))

    with open('appIdList.txt', 'w') as file:
        json.dump(array, file)

    return True


def update_data():
    print("-------------------------------")
    print("Updating Data")
    with open('appIdList.txt', 'r') as file:
        array = json.loads(file.read())
    print('The first item of the List is ' + array[0])

    for item in array:
        result = update_game_data(item)
        if (result):
            print('SUCCESS')

    return True


def update_game_data(appid):
    print("-------------------------------")
    print("Updating game data of " + str(appid))
    game = []
    steamSpy_data = get_steamSpy_data(appid)
    if(steamSpy_data == False):
        return False
    game += steamSpy_data

    steamAPI_data = get_steamAPI_data(appid)
    if(steamAPI_data == False):
        return False
    game += steamAPI_data

    steamCharts_data = get_steamCharts_data(appid)
    if(steamCharts_data == False):
        return False
    game += steamCharts_data

    steamHistory_data = get_steamHistory_data(appid)
    if(steamHistory_data == False):
        return False
    game += steamHistory_data

    update_database(game)
    print(game)
    return True


def get_steamSpy_data(appid):
    url = 'https://steamspy.com/api.php?request=appdetails&appid=' + str(appid)
    steamSpy = []
    try:
        response = urlopen(url)
    except HTTPError as error:
        print('Data not found in steamSpy')
        return False
    except URLError as error:
        print(error.reason)
        return False
    data = json.loads(response.read())

    steamSpy.append(data.get('appid'))
    steamSpy.append(data.get('name'))
    steamSpy.append(data.get('publisher'))
    steamSpy.append(data.get('positive'))
    steamSpy.append(data.get('negative'))
    steamSpy.append(data.get('languages'))
    steamSpy.append(data.get('tags'))
    steamSpy.append(Scrap_algorithm.get_followers(appid))

    print('- SteamSpy done')

    return steamSpy


def get_steamAPI_data(appid):
    url = 'https://store.steampowered.com/api/appdetails/get?appids=' + \
        str(appid)
    steamAPI = []
    try:
        response = urlopen(url)
    except HTTPError as error:
        print('Data not found in steamAPI')
        return False
    except URLError as error:
        print(error.reason)
        return False
    data = json.loads(response.read())
    data = data.get(appid).get('data')

    steamAPI.append(data.get('required_age'))
    steamAPI.append(data.get('is_free'))
    steamAPI.append(data.get('platforms'))
    if(data.get('metacritic')):
        print('- Metacritic done')
        steamAPI.append(Scrap_algorithm.scrap_metacritic(
            data.get('metacritic').get('url')))
    else:
        steamAPI.append(data.get('metacritic'))
    steamAPI.append(data.get('categories'))
    steamAPI.append(data.get('genres'))
    steamAPI.append(data.get('release_date').get('date'))

    print('- SteamAPI done')

    return steamAPI


def get_steamCharts_data(appid):
    steamCharts = []
    data_steamCharts = Scrap_algorithm.scrap_steamCharts(appid)
    if(data_steamCharts == False):
        return False
    steamCharts += data_steamCharts

    print('- SteamCharts done')

    return steamCharts


def get_steamHistory_data(appid):
    steamHistory = []
    data_steamHistory = Scrap_algorithm.scrap_steamPrice(appid)
    if(data_steamHistory == False):
        return False
    steamHistory += data_steamHistory

    print('- SteamHistory done')

    return steamHistory


def update_database(game):
    print("Ready to save in DB!")

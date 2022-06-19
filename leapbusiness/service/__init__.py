import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from .Scrap_algorithm import Scrap_algorithm
from .Service_format import Service_format
from domain.Game import Game

# main() : true | false -> Success
#   update_steamSpy_list() : true | false -> Success
#   update_data(appIdList: array) : true | false -> Success
#       update_game_data(appid: appIdList[i]) : true | false -> Success
#           url = "https" + appid
#           get_steamSpy_data(appid) : steamSpy class or array
#           get_steamAPI_data(appid) : steamAPI class or array
#               get_metacritic_data(aux.url) : metacritic class or array
#           get_steamCharts_data(appid) : steamCharts class or array
#           get_steamHistory_data(appid) : steamHistory class or array
#           print()
#           update_database(game class) : true | false -> Success
#


def main():
    start = time.time()
    print("-------------------------------")
    print("Main")
    update_steamSpy_list()
    update_data()
    end = time.time()
    print("-------------------------------")
    print('Total time elapsed: ')
    print(start-end)
    return True


def update_steamSpy_list():
    print("-------------------------------")
    print("Updating List")
    url = 'https://steamspy.com/api.php?request=all&page='
    list = []
    count = 0
    max_error_count = 10
    status_code = 200

    while(status_code == 200 and max_error_count > 0):
        try:
            response = urlopen(url + str(count))
            status_code = response.getcode()
            items = json.loads(response.read())
            for item in items:
                list.append(item)
            count += 1
        except HTTPError as error:
            print("Error while updating steamSpy list")
            print(error.status, error.reason)
            print("Retrying...")
            max_error_count -= 1
            continue
        except URLError as error:
            print(error.reason)
            print("Retrying...")
            max_error_count -= 1
            continue

    print('No response from page ' + str(count))

    if (list != []):
        with open('appIdList.txt', 'w') as file:
            json.dump(list, file)
            print('Updated list')
        return True

    print('The responses were probably empty, so the list was not updated')
    return False


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
    game.append(steamCharts_data)

    steamHistory_data = get_steamHistory_data(appid)
    if(steamHistory_data == False):
        return False
    game.append(steamHistory_data)

    gameClass = Game(appId=game[0], name=game[1], publisher=game[2], positive=game[3], negative=game[4], languages=game[5], tags=game[6], followers=game[7], required_age=game[8],
                     is_free=game[9], platforms=game[10], url=game[11], categories=game[12], genres=game[13], release_date=game[14], metacritic=game[15], players=game[16], prices=game[17])
    update_database(gameClass)
    return True


def get_steamSpy_data(appid):
    url = 'https://steamspy.com/api.php?request=appdetails&appid=' + str(appid)
    steamSpy = []
    max_error_count = 10

    while(max_error_count > 0):
        try:
            response = urlopen(url)
            data = json.loads(response.read())
            if(data.get('name') == '' or data.get('name') == None or data.get('tags') == '' or data.get('tags') == None or Scrap_algorithm.get_followers(appid) == None):
                print('Incomplete SteamSpy data')
                return False
            steamSpy.append(data.get('appid'))
            steamSpy.append(data.get('name'))
            steamSpy.append(Service_format.string_to_list(
                data.get('publisher')))
            steamSpy.append(data.get('positive'))
            steamSpy.append(data.get('negative'))
            steamSpy.append(Service_format.string_to_list(
                data.get('languages')))
            steamSpy.append(Service_format.format_Tags(data.get('tags')))
            steamSpy.append(Scrap_algorithm.get_followers(appid))
            print('- SteamSpy done')
            return steamSpy
        except HTTPError as error:
            print('Data not found in steamSpy')
            return False
        except URLError as error:
            print(error.reason)
            return False
        except:
            print('No response, waiting 10 seconds...')
            time.sleep(10)
            max_error_count -= 1
            print('Retrying...')

    print('- SteamSpy data not found')
    return False


def get_steamAPI_data(appid):
    url = 'https://store.steampowered.com/api/appdetails/get?appids=' + \
        str(appid)
    steamAPI = []
    max_error_count = 10

    while(max_error_count > 0):
        try:
            response = urlopen(url)
            data = json.loads(response.read())
            data = data.get(str(appid)).get('data')
            if(data.get('categories') == '' or data.get('categories') == None or data.get('genres') == '' or data.get('genres') == None):
                print('Incomplete SteamAPI data')
                return False
            steamAPI.append(data.get('required_age'))
            steamAPI.append(data.get('is_free'))
            steamAPI.append(Service_format.format_Platforms(
                data.get('platforms')))
            if(data.get('metacritic')):
                steamAPI.append(data.get('metacritic').get('url'))
            else:
                steamAPI.append(data.get('metacritic'))
                print('- Metacritic url not found')
            steamAPI.append(Service_format.format_Categories(
                data.get('categories')))
            steamAPI.append(Service_format.format_Genres(data.get('genres')))
            steamAPI.append(Service_format.format_date_SteamAPI(
                data.get('release_date').get('date')))
            if(data.get('metacritic')):
                steamAPI.append(Scrap_algorithm.scrap_metacritic(
                    data.get('metacritic').get('url')))
            else:
                steamAPI.append(data.get('metacritic'))
                print('- Metacritic data not found')
            print('- SteamAPI done')
            return steamAPI
        except HTTPError as error:
            print('Data not found in steamAPI')
            return False
        except URLError as error:
            print(error.reason)
            return False
        except:
            print('No response, waiting 10 seconds...')
            time.sleep(10)
            max_error_count -= 1
            print('Retrying...')

    print('- SteamAPI data not found')
    return False


def get_steamCharts_data(appid):
    data_steamCharts = Scrap_algorithm.scrap_steamCharts(appid)
    if(data_steamCharts == False):
        return None

    print('- SteamCharts done')

    return data_steamCharts


def get_steamHistory_data(appid):
    data_steamHistory = Scrap_algorithm.scrap_steamPrice(appid)
    if(data_steamHistory == False):
        return None

    print('- SteamHistory done')

    return data_steamHistory


def update_database(game):
    print("Ready to save in DB!")

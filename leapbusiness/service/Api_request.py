import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from .utils import api_request
from .Service_format import Service_format
from .Scrap_algorithm import Scrap_algorithm
from leapbusiness.domain.Data_Metacritic import DataMetacritic


def steamSpy_data(appid):
    url = 'https://steamspy.com/api.php?request=appdetails&appid=' + str(appid)

    try:
        data = api_request(url)

        if(data.get('name') == '' or data.get('name') == None or data.get('tags') == '' or data.get('tags') == None or Scrap_algorithm.get_followers(appid) == None):
            print('Incomplete SteamSpy data')
            return False

        steamSpy = []
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
    except:
        print('- SteamSpy data not found')
        return False


def steamAPI_data(appid):
    url = 'https://store.steampowered.com/api/appdetails/get?appids=' + \
        str(appid)

    try:
        data = api_request(url)
        data = data.get(str(appid)).get('data')

        if(data.get('categories') == '' or data.get('categories') == None or data.get('genres') == '' or data.get('genres') == None):
            print('Incomplete SteamAPI data')
            return False

        steamAPI = []
        steamAPI.append(data.get('required_age'))
        steamAPI.append(data.get('is_free'))
        steamAPI.append(Service_format.format_Platforms(
            data.get('platforms')))
        if(data.get('metacritic')):
            steamAPI.append(data.get('metacritic').get('url'))
        else:
            steamAPI.append(data.get('metacritic'))
        steamAPI.append(Service_format.format_Categories(
            data.get('categories')))
        steamAPI.append(Service_format.format_Genres(data.get('genres')))
        steamAPI.append(Service_format.format_date_SteamAPI(
            data.get('release_date').get('date')))
        if(data.get('metacritic')):
            steamAPI.append(Scrap_algorithm.scrap_metacritic(
                data.get('metacritic').get('url')))
        else:
            steamAPI.append(DataMetacritic())
            print('- Metacritic data not found')

        print('- SteamAPI done')

        return steamAPI
    except:
        print('- SteamAPI data not found')
        return False


def steamSpy_list():
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
            print(count)
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

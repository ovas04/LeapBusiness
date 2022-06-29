import json
from statistics import mean
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from flask import g

from numpy import empty
from .Scrap_algorithm import Scrap_algorithm
from .Service_format import Service_format
from domain.Game import Game
import psycopg2


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

total_games = 0
total_fallos = 0

def main():
    start = time.time()
    print("-------------------------------")
    print("Main")
    #update_steamSpy_list()
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


def update_data():
    print("-------------------------------")
    print("Updating Data")
    with open('appIdList.txt', 'r') as file:
        array = json.loads(file.read())
    print('The first item of the List is ' + array[0])

    for item in array:
        result = update_game_data(item)
        if (result):

            print('-----END PROCESS GAME------- \n')

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

    #steamHistory_data = get_steamHistory_data(appid)
    #if(steamHistory_data == False):
    #    return False
    #game.append(steamHistory_data)

    gameClass = Game(appId=game[0], name=game[1], publisher=game[2], positive=game[3], negative=game[4], languages=game[5], tags=game[6], followers=game[7], required_age=game[8],
                     is_free=game[9], platforms=game[10], url=game[11], categories=game[12], genres=game[13], release_date=game[14], metacritic=game[15], players=game[16], prices=None)#, prices=game[17])
    update_database(gameClass)
    return True


def get_steamSpy_data(appid):
    url = 'https://steamspy.com/api.php?request=appdetails&appid=' + str(appid)
    steamSpy = []
    max_error_count = 3

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
    max_error_count = 3

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

    hostname = 'localhost'
    database = 'db_leapbusiness'
    username = 'postgres'
    pwd = 'Idranoide11'
    port_id = 5432


    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password= pwd,
            port = port_id )


    my_cursor = conn.cursor()
    
    #Validations-----------------

    #-----------------------------
  
    print(game.metacritic)
    print(game.is_free)
    print(game.followers)
    print(game.mean_price)

    if(game.is_free == False and game.followers > 200 and game.mean_price > 0):

        my_cursor.execute("CALL leapbusiness.sp_register_update_videogame(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (int(game.appId),str(game.name),game.total_recommendations, str(game.required_age), bool(game.is_free), game.followers, game.url,game.release_date,
            game.lower_price, game.upper_price,game.mean_price, game.metacritic.userScore, game.metacritic.metaScore, game.total_sales))


        conn.commit()


        for category in game.categories:
            my_cursor.execute("CALL leapbusiness.sp_register_categories(%s,%s,%s)",(
                                game.appId, category.id, category.desc))
            

        conn.commit()

        
        for genre in game.genres:
            my_cursor.execute("CALL leapbusiness.sp_register_genre(%s,%s,%s)",(
                                    game.appId, genre.id, genre.desc))   

        conn.commit()

        

        for tag in game.tags:
            my_cursor.execute("CALL leapbusiness.sp_register_tags(%s,%s,%s)",(
                                    game.appId, tag.id, tag.desc))   

        conn.commit()

        for language in game.languages:
            my_cursor.execute("CALL leapbusiness.sp_register_game_language( %s, %s)",(
                                    game.appId, language))   

        conn.commit()


        for platform in game.platforms:

            if(platform.state == True):

                my_cursor.execute("CALL leapbusiness.sp_register_platforms( %s, %s)",(
                                game.appId, platform.desc))   

        conn.commit()


        for publisher in game.publisher:
            my_cursor.execute("CALL leapbusiness.sp_register_publishers( %s, %s)",(
                                    game.appId, publisher))   

        conn.commit()

        my_cursor.execute("CALL leapbusiness.sp_register_recomendations( %s, %s, %s)",(
                                    game.appId, "positive", game.positive))   

        conn.commit()


        my_cursor.execute("CALL leapbusiness.sp_register_recomendations( %s, %s, %s)",(
                                    game.appId, "negative", game.negative))   

        conn.commit()

        if(game.metacritic.genres != None):    

            for genre_user in game.metacritic.genres:
                my_cursor.execute("CALL leapbusiness.sp_register_genre_user( %s, %s)",(
                                        game.appId, genre_user))   

            conn.commit()
        


        if(bool(game.prices) != False):
            
            for price in game.prices:
                my_cursor.execute("CALL leapbusiness.sp_register_prices(%s,%s,%s)",
                            (game.appId, price.date_price, price.price))

                conn.commit()


        if(bool(game.players) != False):
            
            for players_data in game.players:
                my_cursor.execute("CALL leapbusiness.sp_register_current_players(%s,%s,%s,%s)",
                        (game.appId, players_data.mounth, players_data.avg_players, players_data.avg_players))

                conn.commit()

        print("Registered in database")
    
    else:

        print("Not registered")

        


    conn.close()




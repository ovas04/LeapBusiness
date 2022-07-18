import json
import time
from .connect import get_connection, get_connection_local
from .Scrap_algorithm import Scrap_algorithm
from .Api_request import steamAPI_data, steamSpy_data, steamSpy_list
from domain.Game import Game


def main():
    try:
        start = time.time()
        print("-------------------------------")
        print("Main")
        # update_steamSpy_list()
        update_data()
        end = time.time()
        print("-------------------------------")
        print('Total time elapsed: ')
        print(start-end)
        print("Total Juegos registrados: " + str(Game.TOTAL_GAMES))
        print("Total Juegos Fallados: " + str(Game.TOTAL_FALLOS))

    except Exception as err:
        print(err)
        Game.FLAG_ERROR = True
        update_data()
        end = time.time()
        print("-------------------------------")
        print('Total time elapsed: ')
        print(start-end)
        print("Total Juegos registrados: " + str(Game.TOTAL_GAMES))
        print("Total Juegos Fallados: " + str(Game.TOTAL_FALLOS))

    start = time.time()
    print("-------------------------------")
    print("Main")
    # update_steamSpy_list()
    update_data()
    end = time.time()
    print("-------------------------------")
    print('Total time elapsed: ')
    print(start-end)
    print("Total Juegos registrados: " + str(Game.TOTAL_GAMES))
    print("Total Juegos Fallados: " + str(Game.TOTAL_FALLOS))
    return True


def update_steamSpy_list():
    print("-------------------------------")
    print("Updating List")
    return steamSpy_list()


def update_data():
    print("-------------------------------")
    print("Updating Data")
    with open('appIdList.txt', 'r') as file:
        array = json.loads(file.read())

    index = 0
    if(Game.FLAG_ERROR):
        index = Game.INDEX

    print('The first item of the List is ' + array[index])

    for i in range(index, len(array)):
        result = update_game_data(array[i])
        if (result):
            print('-----END PROCESS GAME------- \n')
            Game.INDEX = Game.INDEX + 1
            print('Juegos registrados por el momendo:  ' +
                  str(Game.TOTAL_GAMES) + '\n')

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

    game.append(get_steamCharts_data(appid))

    game.append(get_steamPrice_data(appid))

    gameClass = Game(appId=game[0], name=game[1], publisher=game[2], positive=game[3], negative=game[4], languages=game[5], tags=game[6], followers=game[7], required_age=game[8],
                     is_free=game[9], platforms=game[10], url=game[11], categories=game[12], genres=game[13], release_date=game[14], metacritic=game[15], players=game[16], prices=game[17])

    print(gameClass)
    update_database(gameClass)
    return True


def get_steamSpy_data(appid):
    return steamSpy_data(appid)


def get_steamAPI_data(appid):
    return steamAPI_data(appid)


def get_steamCharts_data(appid):
    return Scrap_algorithm.scrap_steamCharts(appid)


def get_steamPrice_data(appid):
    return Scrap_algorithm.scrap_steamPrice(appid)


def update_database(game):

    # Validations

    print("GAME METACRITIC = " + str(game.metacritic))
    print("IS FREE : " + str(game.is_free))
    print("FOLLOWERS : " + str(game.followers))
    print("MEAN_PRICE : " + str(game.mean_price))
    print("URL_METACRITIC : " + str(game.url))

    if(game.is_free == False and game.followers > 1000 and game.mean_price > 0):

        register_game_db(game)

    else:
        Game.TOTAL_FALLOS = Game.TOTAL_FALLOS + 1
        print("Not registered")


def register_game_db(game):
    conn = get_connection()
    my_cursor = conn.cursor()

    my_cursor.execute("CALL leapbusiness.sp_register_update_videogame(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                      (int(game.appId), str(game.name), game.total_recommendations, str(game.required_age), bool(game.is_free), game.followers, game.url, game.release_date, game.lower_price, game.upper_price, game.mean_price, game.metacritic.userScore, game.metacritic.metaScore, game.total_sales))

    conn.commit()

    for category in game.categories:
        my_cursor.execute("CALL leapbusiness.sp_register_categories(%s,%s,%s)", (
            game.appId, category.id, category.desc))

    conn.commit()

    for genre in game.genres:
        my_cursor.execute("CALL leapbusiness.sp_register_genre(%s,%s,%s)", (
            game.appId, genre.id, genre.desc))

    conn.commit()

    for tag in game.tags:
        my_cursor.execute("CALL leapbusiness.sp_register_tags(%s,%s,%s)", (
            game.appId, tag.id, tag.desc))

    conn.commit()

    for language in game.languages:
        my_cursor.execute("CALL leapbusiness.sp_register_game_language( %s, %s)", (
            game.appId, language))

    conn.commit()

    for platform in game.platforms:

        if(platform.state == True):

            my_cursor.execute("CALL leapbusiness.sp_register_platforms( %s, %s)", (
                game.appId, platform.desc))

        conn.commit()

    for publisher in game.publisher:
        my_cursor.execute("CALL leapbusiness.sp_register_publishers( %s, %s)", (
            game.appId, publisher))

    conn.commit()

    my_cursor.execute("CALL leapbusiness.sp_register_recomendations( %s, %s, %s)", (
        game.appId, "positive", game.positive))

    conn.commit()

    my_cursor.execute("CALL leapbusiness.sp_register_recomendations( %s, %s, %s)", (
        game.appId, "negative", game.negative))

    conn.commit()

    if(game.metacritic.genres != None):

        for genre_user in game.metacritic.genres:
            my_cursor.execute("CALL leapbusiness.sp_register_genre_user( %s, %s)", (
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
                              (game.appId, players_data.mounth, players_data.avg_players, players_data.peak_players))

        conn.commit()

    Game.TOTAL_GAMES = Game.TOTAL_GAMES + 1
    print("Registered in database")

    my_cursor.execute("CALL leapbusiness.sp_validation_prices(%s)",(game.appId,))
    my_cursor.execute("CALL leapbusiness.sp_anex_recommendations(%s)",(game.appId,))

    conn.close()


def register_prices_db(game):
    conn = get_connection()
    my_cursor = conn.cursor()

    if(bool(game.prices) != False):

        for price in game.prices:
            my_cursor.execute("CALL leapbusiness.sp_register_prices(%s,%s,%s)",
                              (game.appId, price.date_price, price.price))

        conn.commit()

    conn.close()


def register_players_db(game):
    conn = get_connection()
    my_cursor = conn.cursor()

    if(bool(game.players) != False):

        for players_data in game.players:
            my_cursor.execute("CALL leapbusiness.sp_register_current_players(%s,%s,%s,%s)",
                              (game.appId, players_data.mounth, players_data.avg_players, players_data.peak_players))

        conn.commit()

    conn.close()


def register_metacritic_db(game):
    conn = get_connection()
    my_cursor = conn.cursor()

    my_cursor.execute("CALL leapbusiness.sp_register_update_videogame(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                      (int(game.appId), str(game.name), game.total_recommendations, str(game.required_age), bool(game.is_free), game.followers, game.url, game.release_date, game.lower_price, game.upper_price, game.mean_price, game.metacritic.userScore, game.metacritic.metaScore, game.total_sales))

    conn.commit()

    if(game.metacritic.genres != None):

        for genre_user in game.metacritic.genres:
            my_cursor.execute("CALL leapbusiness.sp_register_genre_user( %s, %s)", (
                game.appId, genre_user))

    conn.commit()

    conn.close()


def update_modular(case):
    print("-------------------------------")
    print("Starting modular update")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT appid from leapbusiness.videogames;")
    appIdList = cur.fetchall()

    match case:
        case 1:
            update_game(appIdList, conn)
        case 2:
            update_metacritic(appIdList, conn)
        case 3:
            update_steamPrice(appIdList, conn)
        case 4:
            update_steamCharts(appIdList, conn)


def update_game(list_appId, conn):
    TOTAL_GAMES_UPDATED = 0

    print('Game Data')

    my_cursor = conn.cursor()

    for appId in list_appId:
        print("-------------------------------")
        game = []

        steamSpy_data = get_steamSpy_data(appId[0])

        if(steamSpy_data == False):
            continue
        game += steamSpy_data

        steamAPI_data = get_steamAPI_data(appId[0])

        if(steamAPI_data == False):
            continue
        game += steamAPI_data

        gameClass = Game(appId=game[0], name=game[1], publisher=game[2], positive=game[3], negative=game[4], languages=game[5], tags=game[6], followers=game[7],
                         required_age=game[8], is_free=game[9], platforms=game[10], url=game[11], categories=game[12], genres=game[13], release_date=game[14])

        if(gameClass.is_free == False and gameClass.followers > 1000 and gameClass.mean_price > 0):
            my_cursor.execute("CALL leapbusiness.sp_update_videogame(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (int(gameClass.appId), str(gameClass.name), gameClass.total_recommendations, str(gameClass.required_age), bool(gameClass.is_free), gameClass.followers, gameClass.url, gameClass.release_date, gameClass.total_sales))

            TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

            print('- Game ' + str(appId[0]) + ' updated')

            conn.commit()

    print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
          str(TOTAL_GAMES_UPDATED))


def update_metacritic(list_appId, conn):
    TOTAL_GAMES_UPDATED = 0

    print('Metacritic')

    my_cursor = conn.cursor()

    for appId in list_appId:
        print("-------------------------------")
        steamAPI_data = get_steamAPI_data(appId[0])

        if(steamAPI_data == False):
            continue

        data = steamAPI_data[7]

        my_cursor.execute("CALL leapbusiness.sp_update_metacritic_videogame(%s,%s,%s)",
                          (appId[0], data.userScore, data.metaScore))

        conn.commit()

        if(data.genres != None):
            for genre_user in data.genres:
                my_cursor.execute("CALL leapbusiness.sp_register_genre_user( %s, %s)", (
                    appId[0], genre_user))

            TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

            print('- Game ' + str(appId[0]) + ' updated')

            conn.commit()

    print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
          str(TOTAL_GAMES_UPDATED))


def update_steamPrice(list_appId, conn):
    TOTAL_GAMES_UPDATED = 0

    print('Steam Price')

    my_cursor = conn.cursor()

    TOTAL_FALTANTES = len(list_appId)


    for appId in list_appId:

        TOTAL_FALTANTES = TOTAL_FALTANTES - 1

        
        print("-------------------------------")
        steamHistory_data = get_steamPrice_data(appId[0])

        if(steamHistory_data is None):
                
            print("FALLO EN RECUPERAR DATOS DE : " + str(appId[0]))
                
                
        else:

            for price in steamHistory_data:
                my_cursor.execute("CALL leapbusiness.sp_register_prices(%s,%s,%s)", (appId[0], price.date_price, price.price))

                conn.commit()



        game = Game(appId=appId[0], name=None, publisher=None, positive=0, negative=0, languages=None, tags=None,  followers=0, required_age=None, is_free=None, platforms=None, url=None, categories=None, genres=None, release_date=None, prices=steamHistory_data)            

        my_cursor.execute("CALL leapbusiness.sp_update_price_videogame(%s,%s,%s,%s)",
                                (game.appId, game.lower_price, game.mean_price, game.upper_price))

        conn.commit()

        TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1
        TOTAL_FALTANTES = TOTAL_FALTANTES - 1

        print('- Game ' + str(appId[0]) + ' updated')
        print('- Game total faltantes :' + str(TOTAL_FALTANTES))
            

        print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
                str(TOTAL_GAMES_UPDATED))


    my_cursor.execute("CALL leapbusiness.sp_validation_prices()")

    conn.commit()


def update_steamCharts(list_appId, conn):
    TOTAL_GAMES_UPDATED = 0

    print('Steam Charts')

    my_cursor = conn.cursor()


    for appId in list_appId:
        print("-------------------------------")
        steamCharts_data = get_steamCharts_data(appId[0])

        if(steamCharts_data is None):
            print("FALLO EN RECUPERAR DATOS DE : " + str(appId[0]))
            continue

        for players_data in steamCharts_data:
            my_cursor.execute("CALL leapbusiness.sp_register_current_players(%s,%s,%s,%s)",
                              (appId[0], players_data.mounth, players_data.avg_players, players_data.peak_players))

            conn.commit()

            TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

            print('- Game ' + str(appId[0]) + ' updated, date : ' + str(players_data.mounth))

    print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
          str(TOTAL_GAMES_UPDATED))

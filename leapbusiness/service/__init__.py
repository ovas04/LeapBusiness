import json
import time
from leapbusiness.domain.Data_Metacritic import DataMetacritic
from .Scrap_algorithm import Scrap_algorithm
from .Api_request import steamAPI_data, steamSpy_data, steamSpy_list
from domain.Game import Game
import psycopg2


def main():

    start = time.time()
    print("-------------------------------")
    print("Main")
    # update_steamSpy_list()
    # update_data()
    update_game_data(578670)
    update_game_data(489240)
    update_game_data(595490)
    update_game_data(584040)
    update_game_data(599430)
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
    print('The first item of the List is ' + array[0])

    for item in array:
        result = update_game_data(item)
        if (result):

            print('-----END PROCESS GAME------- \n')
            print('Juegos registrados por el momendo:  ' + str(Game.TOTAL_GAMES))

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
    # update_database(gameClass)
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

    hostname = 'localhost'
    database = 'db_leapbusiness'
    username = 'postgres'
    pwd = 'Idranoide11'
    port_id = 5432

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

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
                              (game.appId, players_data.mounth, players_data.avg_players, players_data.avg_players))

        conn.commit()

    Game.TOTAL_GAMES = Game.TOTAL_GAMES + 1
    print("Registered in database")

    conn.close()


def register_prices_db(game):

    hostname = 'localhost'
    database = 'db_leapbusiness'
    username = 'postgres'
    pwd = '***'
    port_id = 5432

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    my_cursor = conn.cursor()

    if(bool(game.prices) != False):

        for price in game.prices:
            my_cursor.execute("CALL leapbusiness.sp_register_prices(%s,%s,%s)",
                              (game.appId, price.date_price, price.price))

        conn.commit()

    conn.close()


def register_players_db(game):

    hostname = 'localhost'
    database = 'db_leapbusiness'
    username = 'postgres'
    pwd = 'Idranoide11'
    port_id = 5432

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    my_cursor = conn.cursor()

    if(bool(game.players) != False):

        for players_data in game.players:
            my_cursor.execute("CALL leapbusiness.sp_register_current_players(%s,%s,%s,%s)",
                              (game.appId, players_data.mounth, players_data.avg_players, players_data.avg_players))

        conn.commit()

    conn.close()


def register_metacritic_db(game):

    hostname = 'localhost'
    database = 'db_leapbusiness'
    username = 'postgres'
    pwd = 'Idranoide11'
    port_id = 5432

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

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

 #! CAMBIO DE BOTONES ------------------------------------------------------


def update_steamCharts(list_appId):

    TOTAL_GAMES_UPDATED = 0

    # TODO INSERTAR CODIGO DE CONNEXION A BASE DE DATOS

    my_cursor = conn.cursor()

    for appId in list_appId:

        steamCharts_data = get_steamCharts_data(appId)

        if(steamCharts_data == False):

            print("FALLO EN RECUPERAR DATOS DE : " + str(appId))

            continue

        if(bool(steamCharts_data) != False):

            for players_data in steamCharts_data:

                my_cursor.execute("CALL leapbusiness.sp_register_current_players(%s,%s,%s,%s)",
                                  (appId, players_data.mounth, players_data.avg_players, players_data.avg_players))

                conn.commit()

                TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

    print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
          str(TOTAL_GAMES_UPDATED))


def update_steamPrice(list_appId):

    TOTAL_GAMES_UPDATED = 0

    # TODO INSERTAR CODIGO DE CONNEXION A BASE DE DATOS

    my_cursor = conn.cursor()

    for appId in list_appId:

        steamHistory_data = get_steamPrice_data(appId)

        if(steamHistory_data == False):

            print("FALLO EN RECUPERAR DATOS DE : " + str(appId))

            continue

        if(bool(steamHistory_data) != False):

            for price in steamHistory_data:

                my_cursor.execute("CALL leapbusiness.sp_register_prices(%s,%s,%s)",
                                  (appId, price.date_price, price.price))

                conn.commit()

                game = Game(appId=appId, prices=steamHistory_data)

                my_cursor.execute("CALL leapbusiness.sp_update_price_videogame(%s,%s,%s,%s)",
                                  (appId, game.lower_price, game.mean_price, game.upper_price))

                conn.commit()

                TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

        print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
              str(TOTAL_GAMES_UPDATED))


def update_metacritic(list_appId):

    TOTAL_GAMES_UPDATED = 0

    # TODO INSERTAR CODIGO DE CONNEXION A BASE DE DATOS

    my_cursor = conn.cursor()

    for appId in list_appId:

        game = Game(appId=appId)

        if(game.metacritic == False):
            game.metacritic = DataMetacritic(None, None, None)

        my_cursor.execute("CALL leapbusiness.sp_update_metacritic_videogame(%s,%s,%s)",
                          (appId, game.metacritic.userScore, game.metacritic.metaScore))

        conn.commit()

        if(game.metacritic.genres != None):

            for genre_user in game.metacritic.genres:
                my_cursor.execute("CALL leapbusiness.sp_register_genre_user( %s, %s)", (
                    game.appId, genre_user))

            TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

            conn.commit()

    print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
          str(TOTAL_GAMES_UPDATED))


def update_game(list_appId):

    TOTAL_GAMES_UPDATED = 0

    # TODO INSERTAR CODIGO DE CONNEXION A BASE DE DATOS

    my_cursor = conn.cursor()

    for appId in list_appId:

        game = []

        steamSpy_data = get_steamSpy_data(appId)

        if(steamSpy_data == False):
            continue
        game += steamSpy_data

        steamAPI_data = get_steamAPI_data(appId)

        if(steamAPI_data == False):
            continue
        game += steamAPI_data

        gameClass = Game(appId=game[0], name=game[1], publisher=game[2], positive=game[3], negative=game[4], languages=game[5], tags=game[6], followers=game[7],
                         required_age=game[8], is_free=game[9], platforms=game[10], url=game[11], categories=game[12], genres=game[13], release_date=game[14])

        if(game.is_free == False and game.followers > 1000 and game.mean_price > 0):

            my_cursor.execute("CALL leapbusiness.sp_update_videogame(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (int(gameClass.appId), str(gameClass.name), gameClass.total_recommendations, str(gameClass.required_age), bool(gameClass.is_free), gameClass.followers, gameClass.url, gameClass.release_date))

            TOTAL_GAMES_UPDATED = TOTAL_GAMES_UPDATED + 1

            conn.commit()

    print("ACTUALIZACON COMPLETA -- TOTAL_GAMES_UPDATED = " +
          str(TOTAL_GAMES_UPDATED))

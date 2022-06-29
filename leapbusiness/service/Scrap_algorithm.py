import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from typing import final
from .Service_format import Service_format

from domain.Data_Metacritic import DataMetacritic
from domain.Data_SteamCharts import DataSteamCharts
from domain.Data_SteamPriceHistory import DataSteamPriceHistory


class Scrap_algorithm:

    @staticmethod
    def scrap_metacritic(url):

        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})

        genres = []

        max_error_count = 3

        while(max_error_count > 0):
            try:
                html = urlopen(expect_request).read()

                object_beautifulSoup = BeautifulSoup(html, "lxml")

                metaScore = object_beautifulSoup.select(
                    'div > div > div > div > a > div > span')[0].get_text()

                userScore = object_beautifulSoup.select(
                    ' div > div > div > div > div > div > a > div')[1].get_text()

                data_genres = object_beautifulSoup.find(
                    'li', {"class": "summary_detail product_genre"})

                data_genres = data_genres.findAll('span')

                for i in data_genres:

                    if(genres.count(i.get_text()) == 0):
                        genres.append(i.get_text())

                genres.pop(0)
                metaScore = Service_format.metacritic_metaScore_to_number(
                    metaScore)
                userScore = Service_format.metacritic_userScore_to_number(
                    userScore)

                data_metacritic = DataMetacritic(
                    metaScore=metaScore, userScore=userScore, genres=genres)

                print('- Metacritic done')

                return data_metacritic
            except HTTPError as error:
                print('Data not found in Metacritic')
                return False
            except URLError as error:
                print(error.reason)
                return False
            except:
                print('No response, waiting 10 seconds...')
                time.sleep(10)
                max_error_count -= 1
                print('Retrying...')

        print('Data not found in Metacritic')
        return None

    @staticmethod
    def scrap_steamCharts(appId):

        url = ("https://steamcharts.com/app/" + str(appId))

        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})

        List_dates = []

        max_error_count = 3

        while(max_error_count > 0):
            try:
                html = urlopen(expect_request).read()
                object_beautifulSoup = BeautifulSoup(html, "lxml")
                dates = object_beautifulSoup.findAll('tr')

                dates.pop(0)

                for row in dates:

                    game_date = row.select("tr > td")[0].get_text().strip()

                    avg_players = row.select("tr > td")[1].get_text()

                    peak_players = row.select("tr > td")[4].get_text()

                    avg_players = Service_format.from_str_to_float(avg_players)
                    peak_players = Service_format.from_str_to_int(peak_players)

                    data = DataSteamCharts(avg_players=avg_players, peak_players=peak_players,
                                           mounth=Service_format.format_date_SteamChart(game_date))

                    List_dates.append(data)

                return List_dates

            except HTTPError as error:
                print('Data not found in SteamCharts')
                return False
            except URLError as error:
                print(error.reason)
                return False
            except:
                print('No response, waiting 10 seconds...')
                time.sleep(10)
                max_error_count -= 1
                print('Retrying...')

        print('Data not found in SteamCharts')
        return False

    @staticmethod
    def scrap_steamPrice(appId):

        url = ("https://steampricehistory.com/app/" + str(appId))

        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})

        list_prices = []

        max_error_count = 3

        while(max_error_count > 0):
            try:
                html = urlopen(expect_request).read()

                object_beautifulSoup = BeautifulSoup(html, "lxml")

                data_prices = object_beautifulSoup.findAll(
                    "table", {"class": "breakdown-table"})[0]

                data_prices = data_prices.findAll("tr")

                for data in data_prices:

                    if(len(data.select("th")) == 0):

                        date_price = data.select("tr > td")[0].get_text()

                        date_price = Service_format.format_date_SteamPrice(
                            date_price)

                        price = data.select("tr > td")[1].get_text()

                        price = Service_format.steam_price_format_float(price)

                        data = DataSteamPriceHistory(
                            date_price=date_price, price=price)

                        list_prices.append(data)

                return list_prices
            except HTTPError as error:
                
                print('Data not found in SteamPriceHistory')

                return False

            except URLError as error:
                print(error.reason)
                return False
            except:
                print('No response, waiting 10 seconds...')
                time.sleep(10)
                max_error_count -= 1
                print('Retrying...')

        print('Data not found in SteamPrice')
        return False


    @staticmethod
    def get_mean_price_steamSpy(appid):

        try:
            print("Searching in SteamSpy")

            url = ("https://steamspy.com/app/" + str(appid))  
    
            expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})
                
            html = urlopen(expect_request).read()
                
            object_beautifulSoup =  BeautifulSoup(html,"lxml")
                
            data = object_beautifulSoup.select('div > div > div > p')[0].get_text()
            
            try:
                if(data.index("Free to Play") > 0):
                
                    return 0.0

            except ValueError:

                print("Doesn't is Free To Play")

            try: 
                index = data.index("Price:") + 8

            except ValueError:

                print("there isn't price")

                return 0.0

                
            mean_price = ""
                
            for i in range(index,len(data)):
                    
                if((ord(data[i]) < 48 or ord(data[i]) > 57) and ord(data[i]) != 46):
                    break
                else:
                     mean_price = mean_price+data[i]
                        
        except HTTPError as error:
            
            print("Price not found in SteamSpy")

            return False

        except URLError as error:

            print(error.reason)
            return False


        return float(mean_price)


    @staticmethod
    def get_followers(appId):

        url = ("https://steamspy.com/app/" + str(appId))

        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})

        total_followers = ""

        max_error_count = 3

        while(max_error_count > 0):
            try:
                html = urlopen(expect_request).read()

                object_beautifulSoup = BeautifulSoup(html, "lxml")

                data = object_beautifulSoup.select(
                    'div > div > div > p')[0].get_text()

                index = data.index("Followers") + 11

                for i in range(index, len(data)):

                    if((ord(data[i]) < 48 or ord(data[i]) > 57) and ord(data[i]) != 44):
                        break
                    else:
                        total_followers = total_followers+data[i]
                return int(total_followers.replace(",", ""))
            except HTTPError as error:
                print('Followers not found in steamSpy')
                return False
            except URLError as error:
                print(error.reason)
                return False
            except:
                print('No response, waiting 10 seconds...')
                time.sleep(10)
                max_error_count -= 1
                print('Retrying...')

        return None

    

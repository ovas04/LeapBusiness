from .Service_format import Service_format
from .utils import scrap_request

from domain.Data_Metacritic import DataMetacritic
from domain.Data_SteamCharts import DataSteamCharts
from domain.Data_SteamPriceHistory import DataSteamPriceHistory


class Scrap_algorithm:

    @staticmethod
    def scrap_metacritic(url):
        try:
            object_beautifulSoup = scrap_request(url)

            metaScore = object_beautifulSoup.select(
                'div > div > div > div > a > div > span')[0].get_text()

            userScore = object_beautifulSoup.select(
                ' div > div > div > div > div > div > a > div')[1].get_text()

            data_genres = object_beautifulSoup.find(
                'li', {"class": "summary_detail product_genre"})

            data_genres = data_genres.findAll('span')

            genres = []
            for i in data_genres:
                if(genres.count(i.get_text()) == 0):
                    genres.append(i.get_text())
            genres.pop(0)
            metaScore = int(metaScore)
            userScore = float(userScore)

            data_metacritic = DataMetacritic(
                metaScore=metaScore, userScore=userScore, genres=genres)

            print('- Metacritic done')

            return data_metacritic
        except:
            print('Data not found in Metacritic')
            return DataMetacritic()

    @staticmethod
    def scrap_steamCharts(appId):
        url = ("https://steamcharts.com/app/" + str(appId))
        try:
            object_beautifulSoup = scrap_request(url)
            dates = object_beautifulSoup.findAll('tr')

            dates.pop(0)

            List_dates = []
            for row in dates:

                game_date = row.select("tr > td")[0].get_text().strip()

                avg_players = row.select("tr > td")[1].get_text()

                peak_players = row.select("tr > td")[4].get_text()

                avg_players = float(avg_players)
                peak_players = int(peak_players)

                data = DataSteamCharts(avg_players=avg_players, peak_players=peak_players,
                                       mounth=Service_format.format_date_SteamChart(game_date))

                List_dates.append(data)

            print('- SteamCharts done')

            return List_dates
        except:
            print('- SteamCharts data not found')
            return None

    @staticmethod
    def scrap_steamPrice(appId):
        url = ("https://steampricehistory.com/app/" + str(appId))
        url_b = "https://web.archive.org/web/20220314123108/https://steampricehistory.com/app/" + \
            str(appId)

        try:
            object_beautifulSoup = scrap_request(url, 1) if scrap_request(
                url, 1) != None else scrap_request(url_b, 1)

            data_prices = object_beautifulSoup.findAll(
                "table", {"class": "breakdown-table"})[0]

            data_prices = data_prices.findAll("tr")

            list_prices = []
            for data in data_prices:
                if(len(data.select("th")) == 0):
                    date_price = data.select("tr > td")[0].get_text()
                    date_price = Service_format.format_date_SteamPrice(
                        date_price)

                    price = data.select("tr > td")[1].get_text()
                    price = Service_format.steam_price_format(price)

                    data = DataSteamPriceHistory(
                        date_price=date_price, price=price)

                    list_prices.append(data)

            print('- SteamPrice done')

            return list_prices
        except:
            print('- SteamPrice data not found')
            return None

    @staticmethod
    def get_mean_price_steamSpy(appid):
        url = ("https://steamspy.com/app/" + str(appid))
        try:
            print("-------------------------------")
            print("Searching in SteamSpy")
            object_beautifulSoup = scrap_request(url)

            data = object_beautifulSoup.select(
                'div > div > div > p')[0].get_text()

            try:
                if(data.index("Free to Play") > 0):
                    return 0.0
            except ValueError:
                print("- Doesn't is Free To Play")
            try:
                index = data.index("Price:") + 8
            except ValueError:
                print("- There isn't price")
                return 0.0

            mean_price = ""
            for i in range(index, len(data)):
                if((ord(data[i]) < 48 or ord(data[i]) > 57) and ord(data[i]) != 46):
                    break
                else:
                    mean_price = mean_price+data[i]

            print("- Mean price recover from SteamSpy")

            return float(mean_price)
        except:
            print("- Price not found in SteamSpy")
            return None

    @staticmethod
    def get_followers(appId):
        url = ("https://steamspy.com/app/" + str(appId))
        try:
            object_beautifulSoup = scrap_request(url)

            data = object_beautifulSoup.select(
                'div > div > div > p')[0].get_text()

            index = data.index("Followers") + 11

            total_followers = ""
            for i in range(index, len(data)):
                if((ord(data[i]) < 48 or ord(data[i]) > 57) and ord(data[i]) != 44):
                    break
                else:
                    total_followers = total_followers+data[i]

            return int(total_followers.replace(",", ""))
        except:
            return None

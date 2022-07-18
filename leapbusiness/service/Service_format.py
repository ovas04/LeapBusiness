from datetime import date
from domain.Tag import Tag
from domain.Platform import Platform
from domain.Category import Category
from domain.Genre import Genre

months = {'Jan': "01", 'Feb': "02", 'Mar': "03", 'Apr': "04", 'May': "05", 'Jun': "06",
          'Jul': "07", 'Aug': "08", 'Sep': "09", 'Oct': "10", 'Nov': "11", 'Dec': "12"}
months_f = {'January': "01", 'February': "02", 'March': "03", 'April': "04", 'May': "05", 'June': "06",
            'July': "07", 'August': "08", 'September': "09", 'October': "10", 'November': "11", 'December': "12"}


class Service_format:

    @staticmethod
    def steam_price_format(price_str):
        return float(price_str.replace("$", ""))

    @staticmethod
    def string_to_list(string: str):
        return string.rsplit(", ")

    @staticmethod
    def format_Tags(dictionary):
        tags = []
        for key, value in dictionary.items():
            tag = Tag(desc=key, id=value)
            tags.append(tag)
        return tags

    @staticmethod
    def format_Platforms(dictionary):
        platforms = []
        for key, value in dictionary.items():
            platform = Platform(desc=key, state=value)
            platforms.append(platform)
        return platforms

    @staticmethod
    def format_Categories(dictionary):
        categories = []
        for value in dictionary:
            category = Category(id=value.get(
                'id'), desc=value.get('description'))
            categories.append(category)
        return categories

    @staticmethod
    def format_Genres(dictionary):
        genres = []
        for value in dictionary:
            genre = Genre(id=int(value.get('id')),
                          desc=value.get('description'))
            genres.append(genre)
        return genres

    @staticmethod
    def format_date_SteamAPI(date_r):

        print(date_r)
        day = date_r.split(" ")[1].replace(",", "")
        month = months[date_r.split(" ")[0]]
        year = date_r.split(" ")[2]

        dateFormat = date(int(year), int(month), int(day))

        return dateFormat

    @staticmethod
    def format_date_SteamChart(game_date):
        if(game_date == "Last 30 Days"):
            game_date = date(date.today().year, date.today().month, 1)
            return game_date

        month = months_f[game_date .split(" ")[0]]
        year = game_date .split(" ")[1]

        game_date = date(int(year), int(month), 1)

        return game_date

    @staticmethod
    def format_date_SteamPrice(price_date):
        month = months_f[price_date.split(" ")[0]]
        year = price_date.split(" ")[2]
        day = price_date.split(" ")[1].replace(",", "")

        date_price = date(int(year), int(month), int(day))

        return date_price

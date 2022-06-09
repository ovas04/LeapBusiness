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
#           update_database([data: class or array]) : true | false -> Success
#

class Game:

    def __init__(self):

        self.data_metracritic = None
        self.data_steamCharts = []
        self.data_steamPriceHisoty = []

    def set_data_metracritic(self, p_data_metracritic):
        self.data_metracritic = p_data_metracritic

    def set_data_steamCharts(self, p_data_steamCharts):
        self.data_steamCharts = p_data_steamCharts

    def set_data_steamPriceHisoty(self, p_data_steamPriceHisoty):
        self.data_steamPriceHisoty = p_data_steamPriceHisoty

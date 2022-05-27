# main() : true | false -> Success
#   update_steamSpy_list() : appIdList
#   update_data(appIdList: array) : true | false -> Success
#       update_game_data(appid: appIdList[i]) : true | false -> Success
#           url = "https" + appIdList[i]
#           get_steamSpy_data(url) : steamSpy class or array
#           get_steamAPI_data(url) : steamAPI class or array
#           get_metacritic_data(url) : metacritic class or array
#           get_steamCharts_data(url) : steamCharts class or array
#           get_steamHistory_data(url) : steamHistory class or array
#
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

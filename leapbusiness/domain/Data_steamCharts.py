from datetime import date

months = {'January' : "01", 'February' : "02",'March' : "03",'April' : "04",'May' : "05",'June' : "06",
          'July' : "07",'August' : "08",'September' : "09",'October' : "10",'November' : "11",'December' : "12"  }


class Data_steamCharts:
    
    def __init__(self, game_date, avg_players, peak_players):
       
        self.game_date = self.formatDate(game_date)
        self.avg_players = avg_players
        self.peak_players = peak_players
    
    def getGameDate(self):
        return self.game_date
        
    def getAvgPlayers(self):
        return self.avg_players 
        
    def getPeakPlayers(self):
        return self.peak_players
    
    def formatDate(self, game_date):
        
        if(game_date == "Last 30 Days"):
            game_date= date(date.today().year, date.today().month, 1)
            return game_date          
        
        month = months[game_date .split(" ")[0]]
        year = game_date .split(" ")[1]

        game_date = date(int(year), int(month),1)
        
        return game_date
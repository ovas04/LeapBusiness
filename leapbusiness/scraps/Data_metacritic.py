
from datetime import date

months = {'January' : "01", 'February' : "02",'March' : "03",'April' : "04",'May' : "05",'June' : "06",
          'July' : "07",'August' : "08",'September' : "09",'October' : "10",'November' : "11",'December' : "12"  }


class Data_metacritic:
    
     def __init__(self, metaScore, userScore):
        self.metaScore = metaScore
        self.userScore = userScore
        self.generes = []
        
     def setGeneres(self, list_generes):
         self.generes = list_generes
         
     def getMetaScore(self):
         return self.metaScore     
     
     def getUserScore(self):
         return  self.userScore
     
     def getGenres(self):
         return self.generes
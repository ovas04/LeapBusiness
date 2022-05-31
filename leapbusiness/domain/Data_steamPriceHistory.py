
from datetime import date

months = {'January' : "01", 'February' : "02",'March' : "03",'April' : "04",'May' : "05",'June' : "06",
          'July' : "07",'August' : "08",'September' : "09",'October' : "10",'November' : "11",'December' : "12"  }


class Data_steamPriceHistory:
    
     def __init__(self, date_price, price):
        self.price = self.formatDate(date_price)
        self.date_price = date_price
        
     def get_date_price(self):
        return self.date_price
    
     def get_price(self):
        return self.price
    
     def formatDate(self,date_price ):
        
        month = months[date_price .split(" ")[0]]
        
        year = date_price .split(" ")[2]
        
        day= date_price.split(" ")[1].replace(",","")

        date_price = date(int(year), int(month),int(day))
        
        return date_price

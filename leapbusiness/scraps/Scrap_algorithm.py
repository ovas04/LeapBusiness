
from sys import flags
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from tracemalloc import Statistic
from typing import final

from leapbusiness.scraps.data_metacritic import Data_metacritic
from leapbusiness.scraps.data_steamCharts import Data_steamCharts
from leapbusiness.scraps.data_steamPriceHistory import Data_steamPriceHistory


class Scrap_algorithm:

    @staticmethod
    def scrap_metacritic(url):
    
        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})
        
        html = urlopen(expect_request).read()
        
        object_beautifulSoup =  BeautifulSoup(html,"lxml")
        
        metaScore = object_beautifulSoup.select('div > div > div > div > a > div > span')[0].get_text()
            
        userScore = object_beautifulSoup.select(' div > div > div > div > div > div > a > div')[1].get_text()

        
        data_generes = object_beautifulSoup.find('li',{"class":"summary_detail product_genre"})
        
        data_generes = data_generes.findAll('span')
        
        generes = []
        
        for i in data_generes:
            
            if(generes.count(i.get_text()) == 0):
                generes.append(i.get_text())
        
        generes.pop(0)
        
        data_metacritic = Data_metacritic(metaScore, userScore)
        
        data_metacritic.setGeneres(generes)
        
        return data_metacritic

    @staticmethod
    def scrap_steamCharts(appId):
    
        url = ("https://steamcharts.com/app/" + str(appId))
        
        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})
        
        html = urlopen(expect_request).read()
        
        object_beautifulSoup =  BeautifulSoup(html,"lxml")
        
        dates = object_beautifulSoup.findAll('tr',{"class":"odd"})
        
        List_dates = []
        
        for row in dates:   

            game_date = row.select("tr > td")[0].get_text().strip()
            
            avg_players = row.select("tr > td")[1].get_text()
            
            peak_players = row.select("tr > td")[4].get_text()
            
            List_dates.append(Data_steamCharts(game_date, avg_players, peak_players))
            
            
        return List_dates


    @staticmethod
    def scrap_steamPrice(appId):
    
        url = ("https://steampricehistory.com/app/" + str(appId))  
        
        expect_request = Request(url, headers={'User-Agent': '  Mozilla/5.0'})
        
        html = urlopen(expect_request).read()
        
        object_beautifulSoup =  BeautifulSoup(html,"lxml")

        data_prices = object_beautifulSoup.findAll("table",{"class":"breakdown-table"})[0]
        
        data_prices = data_prices.findAll("tr")
        
        list_prices = []
        
        
        for data in data_prices:
            
            if(len(data.select("th")) == 0):
                
                date_price = data.select("tr > td")[0].get_text()
                
                price = data.select("tr > td")[1].get_text()
                
                list_prices.append(Data_steamPriceHistory(date_price, price))
        
        return list_prices
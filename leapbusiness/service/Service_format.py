
class Service_format:
    
    @staticmethod
    def steam_charts_players_to_number(players_str):
        
        players_float= float(players_str)
        
        return players_float
        
    @staticmethod
    def metacritic_metascore_to_number(metascore_str):
           
        metascore_int= int(metascore_str)
        
        return metascore_int   

    @staticmethod
    def metacritic_userscore_to_number(userscore_str):
           
        userscore_float= float(userscore_str)
        
        return userscore_float   
    
    @staticmethod
    def steam_price_format_float(price_str):
       
        price_float = float(price_str.replace("$",""))
        
        return price_float
   
    @staticmethod
    def steam_spy_followers_to_number(followers_str):
       
       followers_float = float(followers_str)
       
       return followers_float
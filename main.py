from requests import Session
from pprint import pprint as pp
from time import strftime
from key import coin_marketcap_api_key


class CMC:
  #https://coinmarketcap.com/api/documentation/v1

  def __init__(self, token):
    self.apiurl = 'https://pro-api.coinmarketcap.com'
    self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
    self.session = Session()
    self.session.headers.update(self.headers)
    
#Prints coin, cotation and hour 
  def __str__(self, symbol):
    price = str(cmc.getPrice(symbol))
    hour, day = self.getDate()
    return (f'\n{symbol} \nUSD {price}\n{hour} - {day}')

#Returns actual time and day
  def getDate(self):
    hour = strftime('%H:%M')
    day = strftime('%d/%m/%Y')
    return hour, day

#Gets all data about the coin
  def getData(self, symbol):
    url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    r = self.session.get(url, params=parameters)
    data = r.json()['data']
    return data

#Treats the data to return only the price.
  def getPrice(self, symbol):
    data = cmc.getData(symbol)
    price = round(data[symbol]['quote']['USD']['price'], 2)
    return price


  def getAllCoins(self):
    url = self.apiurl + '/v1/cryptocurrency/map'
    r = self.session.get(url)
    data = r.json()['data']
    return data



#Generates session
cmc = CMC(coin_marketcap_api_key)


#pp(cmc.getAllCoins())

#Change the coin symbol to get its atual cotation
print(cmc.__str__('FIL'))
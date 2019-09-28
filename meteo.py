
import requests

ville = input('Nom de la ville? :')
api_url ='http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=api_key'
data = requests.get(api_url)
result = [data.json()]


print(result)

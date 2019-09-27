import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=aaab56eafe22118d2cdf76afcf834026='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['base']
print("Current Temp=",json_data['main']['temp']-273.15)
print("Pressure=",json_data['main']['pressure'])
print("Humidity=",json_data['main']['humidity'])
print("MIN TEMP=",json_data['main']['temp_min']-273.15)
print("MAX TEMP=",json_data['main']['temp_max']-273.15)

from urllib import response # pip install urllib3
import requests # pip install requests
api_key="Enter-your-api-key-which-you-get-from-open-weather"

url="http://api.openweathermap.org/data/2.5/weather?"
city=input("City name\n")          
c_url=url+"appid="+api_key+'&q='+city
response=requests.get(c_url)
x=response.json()
if x["cod"]!="404":
    y=x["main"]
    current_temp=y["temp"]
    celcius=int(current_temp)-273.15  # I converted temperature farnheit to celcius for my convenience
    r=str(celcius)
    v=r[:2]
    z=x["weather"]
    weather_descricption=z[0]["description"]
    print(f"It's {v}℃\nToday's weather {weather_descricption}")
else:
    print("not found")

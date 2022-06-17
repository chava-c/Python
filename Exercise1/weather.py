from codecs import latin_1_decode
import requests

key = 'a19913b0ea32583092ca45f0af7e0e1e'

city = 'Guadalajara'

lat = 20.6667

lon = -103.3333

weather_prec = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={key}&units=metric")

#print(weather_prec.json())

weather_raw = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")

#print(weather_raw.json())

country = weather_raw.json()['sys']['country']

weather = weather_raw.json()['weather'][0]['description']

temp = weather_raw.json()['main']['temp']

precp = weather_prec.json()['daily'][0]['pop']
precp = precp*100

print(f"Weather report for: {city}, {country}")
print(f"                    {weather}")
print(f"                    {temp} °C")
print(f"                    {precp}%")


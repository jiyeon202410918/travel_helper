# weather.py

import requests

def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=kr"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return temp, weather_desc
    else:
        return None, "날씨 정보를 불러올 수 없습니다."

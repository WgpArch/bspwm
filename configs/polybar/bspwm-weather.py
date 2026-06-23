#!/usr/bin/env python3

import requests

api_key = '1e0490c09bb5e84b1b8c870abe5bbaad'
city = 'Odendaalsrus,ZA'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description'].title()
        output = f"{temp:.0f}°C {description}"
        print(output)
    else:
        print("Weather Error")
except Exception as e:
    print("Offline")

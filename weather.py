import re

import requests
from bs4 import BeautifulSoup

# provide city of station
city = "San Jose"

# getting raw data
url = "https://www.google.com/search?q=weather" + re.compile('[^a-zA-Z]').sub('', city)
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
temp = int(re.compile('[^1-9]').sub('', temp))

#  time and sky description
time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = time_sky.split('\n')
time = data[0]
sky = data[1].lower()

webdata = f'''
Hello {city}!\n
The time is {time}.\n
The weather is {sky}.\n
The temperature is {temp}°F.\n
'''

# extra friendly messages
if sky == "sunny" and 60 < temp < 80 and (
        (int(time[-8:-6]) >= 6 and time[-2:] == "AM") or (int(time[-8:-6]) <= 6 and time[-2:] == "PM")):
    webdata += "It's a wonderful day for a walk in the park!"
elif "rain" in sky.lower():
    webdata += "Stay cozy in doors folks!"

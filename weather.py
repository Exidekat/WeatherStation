import re

import requests
import pytest
from bs4 import BeautifulSoup

# provide city of station
city = "albany"

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

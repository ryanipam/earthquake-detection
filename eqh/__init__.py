"""
This package use request and beautifulSoup4 for get data
source data scrape is from https://eathquake.usgs.gov
"""
import requests
from bs4 import BeautifulSoup


def getData():
    # Url data scrape
    url = 'https://earthquake.usgs.gov/earthquakes/map/?extent=-80.2385,133.59375&extent=84.9901,500.97656'
    url2 = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    try:
        r = requests.get(url2)
    except Exception:
        return None

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        # listData = soup.find('usgs-events-list', {'class': 'ng-star-inserted'})
        #
        # for i in listData:
        #     print(i)
        print(soup)
        # print(listData)


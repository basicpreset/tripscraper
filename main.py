# First we want to collect the inital website html
# This is the main file responsible for central processing of request and
# maintenance of the central contacts list

# 1. Get all URLs from all cities
# 2. Assigning soup to find all available restaurant profiles on current page
# 3. If index is greater or equal to size of the restaurant URLs list get
# ... new Soup instance and update the restaurant URL list

from bs4 import BeautifulSoup
import urllib.request as request
import city_parser as parser
import urllib
import requests


def main(base_url):
    page = requests.get(base_url, headers={'User-Agent': "Mozilla/5.0"}).text
    soup = BeautifulSoup(page, 'html.parser')

    cities = []
    pageCounter = 1
    switch = False

    for location in soup.find_all('div', {'class': 'geo_name'}):
        for clear_location in location.find_all('a'):
            city_url = clear_location.get('href')
            if '/Restaurants' in city_url:
                cities.append(city_url)
                print(city_url)

        for i in cities:
            parser.collectCity(i)


if __name__ == "__main__":
    main('https://www.tripadvisor.com/Restaurants-g274881-Hungary.html')
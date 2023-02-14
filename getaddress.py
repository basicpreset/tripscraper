from bs4 import BeautifulSoup
import urllib.request as request
import requests

def get(url):
    html_content = requests.get(url, headers={'User-Agent': "Mozilla/5.0"}).text
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        link_x = link.get('href')
        if link_x == "#MAPVIEW":
            # print(link.text)
            return link.text
from bs4 import BeautifulSoup
import urllib.request as request

def get(url):
    html_content = request.urlopen(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        link_x = link.get('href')
        if link_x == "#MAPVIEW":
            # print(link.text)
            return link.text
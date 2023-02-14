from bs4 import BeautifulSoup
import urllib.request
import requests;

# header_format = 'top-info-header'

### Checking the business page for Business Name and returning it
def getBusiness(url):
    html_page = requests.get(url, headers={'User-Agent': "Mozilla/5.0"}).text
    soup = BeautifulSoup(html_page, 'html.parser')
    header = soup.find('h1', {'data-test-target':"top-info-header"})
    return header.text.strip()

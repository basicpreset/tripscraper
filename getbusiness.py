from bs4 import BeautifulSoup
import urllib.request

# header_format = 'top-info-header'

### Checking the business page for Business Name and returning it
def getBusiness(url):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    header = soup.find('h1', {'class':"header heading masthead masthead_h1"})
    return header.text.strip()

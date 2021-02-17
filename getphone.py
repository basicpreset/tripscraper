from bs4 import BeautifulSoup
import urllib.request

phone_number_format = 'tel:'

### Checking the business page for phone number and returning it
def getPhone(site_url):
    html_page = urllib.request.urlopen(site_url)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        element = str(link.get('href'))
        if phone_number_format in element:
            a = element
            b = a.replace(phone_number_format, '')
            return b

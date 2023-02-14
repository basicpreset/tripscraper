from bs4 import BeautifulSoup
import urllib.request
import requests;

phone_number_format = 'tel:'
email_format = 'mailto:'

### Checking the business page for phone number and returning it
def getPhone(site_url):
    html_page = requests.get(site_url, headers={'User-Agent': "Mozilla/5.0"}).text
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        element = str(link.get('href'))
        if phone_number_format in element:
            a = element
            b = a.replace(phone_number_format, '')
            return b

def getEmail(site_url):
    html_page = requests.get(site_url, headers={'User-Agent': "Mozilla/5.0"}).text
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        element = str(link.get('href'))
        if email_format in element:
            a = element
            b = a.replace(email_format, '')
            return b

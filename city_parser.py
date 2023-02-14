from bs4 import BeautifulSoup
import urllib.request as request
import requests;


def collectCity(city_url_extension):
    website_base_url = 'https://www.tripadvisor.co.hu'
    full_url = website_base_url + city_url_extension
    html_file = requests.get(full_url, headers={'User-Agent': "Mozilla/5.0"}).text
    soup = BeautifulSoup(html_file, 'html.parser')

    restaurant_url_format = 'Restaurant_Review'

    restaurant_list = []

    # Get page length
    page_length = 0
    for link in soup.find_all('a'):
        link_a = link.get('href')
        if link_a is not None and restaurant_url_format in link_a and not "#REVIEWS" in link_a:
            page_length += 1

    print('PAGE LENGTH: ' + str(page_length))

    state_counter = 0
    # This element adds every restaurant on current page to a list
    for link in soup.find_all('a'):
        link_a = link.get('href')
        if link_a is not None and restaurant_url_format in link_a and not "#REVIEWS" in link_a:
            restaurant_list.append(link_a)
            print(restaurant_list)
            if state_counter < page_length - 1:
                state_counter += 1
            else:
                print('Reached end of list, switching page...')
                # This element detects whether there is a next button or not
                if soup.find('a', {'class': 'nav next rndBtn ui_button primary taLnk'}) is not None:
                    restaurant_list = list(dict.fromkeys(restaurant_list))
                    f = open("restaurants_raw.txt", "a")
                    for restaurant in restaurant_list:
                        f.write(str(restaurant)+'\n')
                    f.close()
                    restart(soup.find('a', {'class': 'nav next rndBtn ui_button primary taLnk'}).get('href'))
                else:
                    print('End of list in this area')

    # This element prints each item in the current page list
    for element in restaurant_list:
        print(element)

def restart(url):
    collectCity(url)

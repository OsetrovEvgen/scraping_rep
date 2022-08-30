from bs4 import BeautifulSoup
import requests
from requests import get
import time
import sendmessage
from sendmessage import sendTelegram


url = 'https://www.tesmanian.com/blogs/tesmanian-blog'
updated_links = ()

while True:
    host = 'https://www.tesmanian.com/'
    url = 'https://www.tesmanian.com/blogs/tesmanian-blog'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    news_data = html_soup.find_all('div', class_='eleven columns omega align_left')
    some_links = host + html_soup.find(class_='eleven columns omega align_left').find('h2').find('a').get('href')

    if some_links != updated_links:
        sendmessage.sendTelegram(some_links)
    else:
        pass

    updated_links = some_links
    time.sleep(15)





# tomas.smit111@gmail.com
# 123456789a
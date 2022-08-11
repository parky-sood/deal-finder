# import libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# url collection
url_dict = ['']

# set up target_url
target_url = 'https://www.newegg.com/p/pl?d=iphone+11+pro'

# open target_url
url_client = urlopen(target_url)

# read, parse page html
page_html = url_client.read()
page_soup = soup(page_html, 'html.parser')

# close url
url_client.close()

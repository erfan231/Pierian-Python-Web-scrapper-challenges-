#                     Goal
#use requests library and BeautifulSoup to connect 
#http://quotes.toscrape.com/ and get the HTML text from the home page


import requests
import bs4


website_url = "http://quotes.toscrape.com/"

website_request = requests.get(website_url)

soup = bs4.BeautifulSoup(website_request.text, "lxml")

print(soup)
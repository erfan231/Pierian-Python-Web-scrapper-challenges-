#Goal - 
#Create a list of all the quotes from the first page

import requests
import bs4 

quotes = []
website_url = "http://quotes.toscrape.com/"

website_request = requests.get(website_url)

soup = bs4.BeautifulSoup(website_request.text, "lxml")

quote_class = soup.select(".text")

for x in quote_class:
    quotes.append(x.text)

print(quotes)
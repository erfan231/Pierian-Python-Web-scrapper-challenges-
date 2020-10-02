#Goal - 
#get the names of all the authors on the home page

import requests
import bs4 

website_url = "http://quotes.toscrape.com/"

website_request = requests.get(website_url)

soup = bs4.BeautifulSoup(website_request.text, "lxml")

class_author = soup.select(".author")
#span_small = span_class.select("small")

for authors in class_author:
    print(authors.text)

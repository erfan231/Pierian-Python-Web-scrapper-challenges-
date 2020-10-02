# Goal - 
#extract the top tags show on the top right side of the page
#hint - keep in mind that theres also tags underneat each quotes

import requests
import bs4 

website_url = "http://quotes.toscrape.com/"

website_request = requests.get(website_url)

tags_soup = bs4.BeautifulSoup(website_request.text, "lxml")

top_10_tags = tags_soup.select(".tag-item")


for top_10 in top_10_tags:
    print(top_10.text)


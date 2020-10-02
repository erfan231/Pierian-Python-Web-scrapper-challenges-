
#Go through all the pages of the website grab the unique authors of the whole website

import requests
import bs4


#one way of doing it if you know how many pages the website has

def solution_one():
    for n in range(1,11):
        website_url = "http://quotes.toscrape.com/page/{}/"
        webiste_request = requests.get(website_url.format(n))
        website_soup = bs4.BeautifulSoup(webiste_request.text, "lxml")
        class_author = website_soup.select(".author")
            #span_small = span_class.select("small")

        for authors in class_author:
            print(authors.text)


#if you don't know how many pages the website has
def solution_two():
   page_valid = True
   pages = 1
   authors = set() # won't save any existing data(dublicates)
   while page_valid:
       website_url = "http://quotes.toscrape.com/page/{}/"
       webiste_request = requests.get(website_url.format(pages))
       website_soup = bs4.BeautifulSoup(webiste_request.text, "lxml")
       if len(website_soup.select(".author")) == 0:
           print(authors)
           page_valid = False
       else:
        website_soup = bs4.BeautifulSoup(webiste_request.text, "lxml")
        class_author = website_soup.select(".author")

        for author in class_author:
            #print(author.text)
            authors.add(author.text)

        #print(authors)

        pages = pages + 1

#solution_one()

solution_two()



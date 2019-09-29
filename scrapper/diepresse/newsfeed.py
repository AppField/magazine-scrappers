from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_newsfeed import Newsfeed

class DiePresseNewsfeed(Newsfeed):
    directory = 'diepresse'

    def query_newsfeed(self):
        aufmacher = self.soup.find('section', {'class': 'block--aufmacher'})
        card_links = aufmacher.find_all('a', {'class': 'card__link'})
        card_hrefs = [ link['href'] for link in card_links]

        items_list = self.soup.find('div', {'class': 'storylist--small'})

        items = items_list.find_all('li', {'class': 'storylist__item'})
        
        base_url = 'https://diepresse.com'
        self.links = [item.find('a')['href'] for item in items]        
        self.links.extend(card_hrefs)


    def write_links(self):
        print(self.links)

class DiePresseMeinungNewsfeed(Newsfeed):
    directory = 'diepresse'

    def query_newsfeed(self):
        aufmacher = self.soup.find('section', {'class': 'block--aufmacher'})
        card_links = aufmacher.find_all('a', {'class': 'card__link'})
        card_hrefs = [ link['href'] for link in card_links]

        items_list = self.soup.find('div', {'class': 'storylist--small'})

        items = items_list.find_all('li', {'class': 'storylist__item'})
        
        base_url = 'https://diepresse.com'
        self.links = [item.find('a')['href'] for item in items]        
        self.links.extend(card_hrefs)


    def write_links(self):
        print(self.links)


def main():
    DiePresseMeinungNewsfeed('https://www.diepresse.com/meinung')

if __name__ == "__main__":
    main()
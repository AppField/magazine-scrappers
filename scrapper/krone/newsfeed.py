from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_newsfeed import Newsfeed

class KurierNewsfeed(Newsfeed):
    directory = 'krone'

    def query_newsfeed(self):
        items = self.soup.find('div', {'class': 'c_newsticker'}).find_all('div', {'class': 'item'})
        
        self.links = [item.find('a')['href'] for item in items]

def main():
    KurierNewsfeed('http://krone.at')

if __name__ == "__main__":
    main()
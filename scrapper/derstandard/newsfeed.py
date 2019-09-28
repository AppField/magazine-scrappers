from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_selenium_newsfeed import SeleniumNewsfeed

class DerStandardNewsfeed(SeleniumNewsfeed):   
    directory= 'derstandard'
    
    def query_newsfeed(self):
        #top_topics = self.soup.find('section', {'class': 'topTopics'})
        container = self.soup.find('div', { 'class': 'chronological'})    
        print(self.soup)
        print(container)
        #articles = container.find_all('article')

        #self.links = [ '{0}{1}'.format(self.url, article['href'].strip()) for article in articles ]

        

def main():
    DerStandardNewsfeed('https://www.derstandard.at/frontpage/latest')

if __name__ == "__main__":
    main()
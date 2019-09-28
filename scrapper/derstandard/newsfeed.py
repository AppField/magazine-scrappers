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
        container = self.soup.find('div', { 'class': 'chronological'})    
        
        articles = container.find_all('article')

        base_url = "https://www.derstandard.at"

        for article in articles:
            href = article.find('a')['href'].strip()
            self.links.append('{0}{1}'.format(base_url, href) if href[0] == "/" else href)


    def browser_preparations(self):
        self.browser.find_element_by_class_name('js-privacywall-agree').click()
        

def main():
    DerStandardNewsfeed('https://www.derstandard.at/frontpage/latest')

if __name__ == "__main__":
    main()
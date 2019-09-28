from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import json
import os
from datetime import datetime
# Necessary to let python find base_article
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_article import BaseArticle

class DiePresseArticle(BaseArticle):
    magazine = 'diepresse'    
    
    def set_meta_data(self):
        #self.article_id = self.soup.find('meta', attrs={'name': 'oct:articleID'})['content']
        self.article_id = re.search('[0-9]+', self.url).group()        

        # get published year and month to create folder hierarchy    
        datestring = self.soup.find('div', attrs={'class': 'meta__date'}).text.strip()
        self.article_published = str(datetime.strptime(datestring, "%d.%m.%Y um %H:%M"))
        
        # get modified to save different versions
        self.article_modified = str(datetime.strptime(datestring, "%d.%m.%Y um %H:%M"))

def main():
    #url = sys.stdin.readline()    
    url = "https://www.diepresse.com/5697555/risse-an-einigen-boeing-737-entdeckt"
    article = DiePresseArticle(url)
    datadoc = article.build_datadoc()
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()
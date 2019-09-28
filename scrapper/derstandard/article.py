from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import json
import os
from datetime import datetime
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
from base_selenium_article import BaseSeleniumArticle

class DerStandardArticle(BaseSeleniumArticle):
    magazine = 'krone'

    def set_meta_data(self):
        self.article_id = re.search('[0-9]+', self.url).group()

        # get published year and month to create folder hierarchy
        p_pub = self.soup.find('p', {'class': 'article-pubdate'})
        if(p_pub):
            datestring = p_pub.find('time')['datetime'].strip()
            self.article_published = str(
                datetime.strptime(datestring, '%Y-%m-%dT%H:%M'))
            self.article_modified = str(
                datetime.strptime(datestring, '%Y-%m-%dT%H:%M'))
        else:
            self.article_published = str(datetime.now())
            self.article_modified = str(datetime.now())

    def browser_preparations(self):
        self.browser.find_element_by_class_name('js-privacywall-agree').click()


def main():
    url = sys.stdin.readline()    
    article = DerStandardArticle(url)
    datadoc = article.build_datadoc()
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()

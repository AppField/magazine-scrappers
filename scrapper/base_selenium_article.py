from bs4 import BeautifulSoup
import sys
import json
import logging
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseSeleniumArticle():
    article_id = ''
    article_published = ''
    article_modified = ''
    magazine = ''
    browser = None

    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup(url)
        self.set_meta_data()

    def get_soup(self, url):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.get(url)

        self.browser_preparations()

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        self.browser.quit()

        return soup

    # Perform action which are neccessary to access the page (like clicking a privacywall button)

    def browser_preparations(self):
        pass

    def set_meta_data(self):
        pass

    def build_datadoc(self):

        article_published = self.article_published[:7]

        # Replace colon with %3A due to HDFS not allowing filenames with colons
        article_modified = self.article_modified.replace(':', '%3A')

        if self.article_id != None:
            return {
                'id': self.article_id,
                'magazine': self.magazine,
                "directory": '{0}/{1}'.format(self.magazine, '/'.join(article_published.split('-'))),
                "filename": '{0}_{1}.json'.format(self.article_id, article_modified),
                'content': str(self.soup)
            }
        else:
            raise Exception("No Article found")

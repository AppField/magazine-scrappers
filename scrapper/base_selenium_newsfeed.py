from bs4 import BeautifulSoup
import urllib.request
import re
import os

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

class SeleniumNewsfeed():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    directory = ''    
    links = [] #array of articles links.Needs to be filled in query_newsfeed function()
    browser = None

    def __init__(self, url):  
        self.last_url_dirname = os.path.join(self.THIS_FOLDER, self.directory, 'last_url.txt')
        self.url = url      
        self.soup = self.get_soup(url)
        self.query_newsfeed()
        self.write_links()

    def get_soup(self, url):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.browser = webdriver.Firefox(options = options)
        self.browser.get(url)

        self.browser_preparations()

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        self.browser.quit()
        
        return soup

    ## Perform action which are neccessary to access the page (like clicking a privacywall button)
    def browser_preparations(self):
        pass

    def query_newsfeed(self):
        pass

    def write_links(self):       
        
        file = open(self.last_url_dirname, 'r+')

        last_url = file.read()
        i = 0
        while i < self.links.__len__() and self.links[i] != last_url:
            print(self.links[i])
            i += 1
        
        file.close()
        file = open(self.last_url_dirname, 'w+') # close and open it in w mode to override content
        if self.links.__len__() > 0:
            file.write(self.links[0])
        file.close()

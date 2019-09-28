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

    def __init__(self, url):  
        self.last_url_dirname = os.path.join(self.THIS_FOLDER, self.directory, 'last_url.txt')
        self.url = url      
        self.soup = self.get_soup(url)
        self.query_newsfeed()
        self.write_links()

    def get_soup(self, url):
        options = webdriver.FirefoxOptions()
        options.headless = True
        browser = webdriver.Firefox(options = options)
        browser.get(url)

        # Wait 10 seconds for page to load
        timeout = 10
      
        browser.find_element_by_class_name('privacywall-overview').click()    
        print('PRIVACY CLICKED')
        
        try:
            # This is not working. An exception is always thrown
            WebDriverWait(browser, timeout).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.chronological')))
            
            print('WEBDRIVERWAIT PASSED')
        except:
            print("Timed out waiting for page to load")
            browser.quit()
        
        print('RETURN SOUP')
        return BeautifulSoup(browser.page_source, 'html.parser')

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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


class SeleniumNewsfeed():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    directory = ''
    links = []  # array of articles links.Needs to be filled in query_newsfeed function()

    def __init__(self, url):
        self.option = webdriver.FirefoxOptions()
        self.option.headless = True
        self.browser = webdriver.Firefox(executable_path="./geckodriver", firefox_options=self.option)
        self.last_url_dirname = os.path.join(self.THIS_FOLDER, self.directory, 'last_url.txt')
        self.url = url
        # self.browser.get(r"https://derstandard.at/?_chron=t")
        self.browser.get(self.url)
        self.query_newsfeed()
        self.write_links()

    def query_newsfeed(self):
        urls = self.browser.find_elements_by_xpath(
            "//div[@id='mainContent']//li[contains(@data-id, '200')]//div[position() = ("
            "last()-1)]//a[parent::h3|parent::h4]")

        links = [x.get_attribute("href") for x in urls]
        return links

    def write_links(self):
        file = open(self.last_url_dirname, 'r+')
        last_url = file.read()
        i = 0
        while i < self.links.__len__() and self.links[i] != last_url:
            print(self.links[i])
            i += 1

        file.close()
        file = open(self.last_url_dirname, 'w+')  # close and open it in w mode to override content
        if self.links.__len__() > 0:
            file.write(self.links[0])
        file.close()

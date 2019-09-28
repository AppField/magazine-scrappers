from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SeleniumBaseArticle():
    article_id = ''
    article_published = ''
    article_modified = ''
    magazine = ''

    def __init__(self, url):
        self.option = webdriver.FirefoxOptions()
        self.option.headless = True
        self.url = url
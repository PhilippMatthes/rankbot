from selenium import webdriver
from time import sleep
from Mailer import Mailer
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = \
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")


class Rankbot:
    def __init__(self):
        self.mailer = Mailer()
        self.url = "https://www.google.de/search?q=philipp+matthes#q=philipp+matthes&start={}"
        self.interval = 600 # 600 seconds
        self.browser = webdriver.PhantomJS(desired_capabilities=dcap)
        self.headlines_xpath = ".//*[@class='r']"

    def get_headlines(self, page):
        self.browser.get(self.url.format(page * 10))
        print(self.url.format(page * 10))
        sleep(3)
        headlines = self.browser.find_elements_by_xpath(self.headlines_xpath)
        for headline in headlines:
            print(headline.text)
        sleep(self.interval)

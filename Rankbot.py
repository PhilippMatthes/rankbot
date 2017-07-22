from selenium import webdriver
from time import sleep
from Mailer import Mailer
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pickle
import matplotlib.pyplot as plt

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = \
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")


class Rankbot:
    def __init__(self):
        with open("sitelog/log.pickle","rb") as logfile:
            self.log = pickle.load(logfile)
        self.mailer = Mailer()
        self.url = "https://www.google.de/search?q={}#q={}&start={}"
        self.browser = webdriver.PhantomJS(desired_capabilities=dcap)
        self.headlines_xpath = ".//*[@class='r']"
        self.targets = {"Philipp Matthes: Imagination Realization" : "philipp+matthes"}


    def find_link(self, page, query, target):
        self.browser.get(self.url.format(query, query, page * 10))
        sleep(3)
        headlines = self.browser.find_elements_by_xpath(self.headlines_xpath)
        index = 0
        for headline in headlines:
            index += 1
            if headline.text == target:
                current_page_number = (page*10)+index
                message = "Found \""+target+"\" on position "+str(current_page_number)
                print(message)

                self.log.append(current_page_number)
                with open("sitelog/log.pickle","wb") as logfile:
                    pickle.dump(self.log, logfile)

                self.mailer.send(message)
                headline.click()
                message = "Clicked link. Current URL: "+self.browser.current_url
                sleep(10)
                return True

        return False


    def search_and_click(self):
        for target, query in self.targets.items():
            for page_number in range(15):
                message = "Current search page: "+str(page_number)
                print(message)
                if self.find_link(page=page_number, query=query, target=target):
                    sleep(60)
                    break
                sleep(60)

    def send_stats(self):
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.plot(self.log)
        save = "sitelog/log.png"
        fig.savefig(save)
        self.mailer.send_image(save)

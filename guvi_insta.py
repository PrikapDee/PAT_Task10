from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Guvi:
    # locators
    xpath_followers = '//li[2]//span[text()="165K"]'
    xpath_following = '//li[3]//div//button//span[text()="6"]'

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # method to get number of followers
    def get_count_followers(self):
        try:
            # open url through get method
            self.driver.get(self.url)
            # maximize window
            self.driver.maximize_window()
            sleep(5)
            # taken a variable name followers and get the location through xpath
            followers = self.driver.find_element(by=By.XPATH, value=self.xpath_followers)

            # print number of followers by using text properly of web element
            print("count of followers is", followers.text)

            return followers.text
        except Exception as e:
            print("error in count of followers ", e)
            return False

    # method to get number of following
    def get_count_following(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(5)
            # variable following and get the location through xpath
            following = self.driver.find_element(by=By.XPATH, value=self.xpath_following)
            # print number of following by using text property of web element
            print("count of following is", following.text)
            return following.text
        except Exception as e:
            print("error in count of followers ", e)
            return False


if __name__ == "__main__":
    url = "https://www.instagram.com/guviofficial/"
    # Creation of Guvi class object
    guvi_obj1 = Guvi(url)
    # call method to count followers
    guvi_obj1.get_count_followers()
    # call method to count following
    guvi_obj1.get_count_following()

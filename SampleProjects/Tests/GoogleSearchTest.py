from time import sleep
import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.options = webdriver.ChromeOptions()
        # cls.options.add_argument("--headless")
        # options = cls.options
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")

        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")

        self.bububa = self.driver.find_element_by_name("btnK")
        sleep(3)
        self.bububa.click()

        print("Title: ", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Finished")


if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HtmlTestRunner.HTMLTestRunner
    (output='C:/Users/Usuario/PycharmProjects/Selenium/testsResults/'))

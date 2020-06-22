import unittest
from time import sleep
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import HtmlTestRunner
from selenium.webdriver import Chrome
from SampleProjects.Pages.LoginPage import LoginPage
from SampleProjects.Pages.MainPage import MainPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.driver.maximize_window()

    def test_Login_Valid(self):
        """Removed for PageObjectModel implementation"""
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # sleep(2)
        # self.driver.find_element_by_link_text("Logout").click()

        # Opening browser
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Login
        login = LoginPage(driver)
        login.enterUsername("Admin")
        login.enterPassword("admin123")
        login.clickLogin()

        # Logout
        homepage = MainPage(driver)
        driver.implicitly_wait(2)
        homepage.clickWelcome()
        driver.implicitly_wait(2)
        homepage.clickLogout()

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Finished test")


if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HtmlTestRunner.HTMLTestRunner
    (output='C:/Users/Usuario/PycharmProjects/Selenium/testsResults/'))

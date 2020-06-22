import HtmlTestRunner
import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://www.google.com")

    def test_search_google(self):
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        self.assertEqual(x, "Automation step by step - Pesquisa Google")

    def test_search_thiago(self):
        self.driver.find_element_by_name("q").send_keys("thiago araujo")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        self.assertEqual(x, "thiago araujo - Pesquisa Google")

    @unittest.skip("This is just a skip test")
    def test_google_other(self):
        """This test will be skipped"""

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Usuario/PycharmProjects/Selenium/testsResults/'),
        verbosity=2)

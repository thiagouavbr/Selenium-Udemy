from selenium import webdriver
import pytest


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        print("Open Website,")
        yield
        print("Logout button,")
        driver.quit()
        print("Finished")

    def test_login(self, test_setup):
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        print("Type user,")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        print("Type passord,")
        driver.find_element_by_id("btnLogin").click()
        print("Button Login,")
        driver.implicitly_wait(5)
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()

    # def test_teardown(self):
    #     print("Logout button,")
    #     driver.quit()
    #     print("Fnished")

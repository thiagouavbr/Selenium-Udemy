from SampleProjects.Pages.Locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver=driver

    def enterUsername(self,username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()

from SampleProjects.Pages.Locators import Locators


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def clickWelcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(Locators.logout_link_text).click()

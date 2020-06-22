from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options =webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.set_page_load_timeout(10)

driver.get("http://www.google.com")
print("Title: ",driver.title)

driver.find_element_by_name("q").send_keys("Automation Step by Step")

"""Wait application"""
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable(By.NAME,"btnK"))
# element.click()

"""Old way of doing the click"""
bububa = driver.find_element_by_name("btnK")
sleep(5)
bububa.click()

driver.close()
driver.quit()
print("Test Finished")
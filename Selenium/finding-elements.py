#########################################
# Finding Elements and Extracting Data
#########################################

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")
element = driver.find_element(By.XPATH, "//a")
element
element.text
print (element.get_attribute("innerHTML"))
print (element.get_attribute("href"))
print (element.get_attribute("innerText"))
print (element.get_attribute("outerHTML"))
print (element.get_attribute("textContent"))

driver.quit()
#########################################
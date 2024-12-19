#########################################
# Finding Elements (Better Approach)
#########################################

from selenium import webdriver
from selenium.webdriver.common.by import By


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://www.example.com")
time.sleep(10)
h1_elem = driver.find_element(By.XPATH, "//h1")
a_elem = driver.find_element(By.XPATH, "//a")
p_elem = driver.find_element(By.XPATH, "//p")
#.....
#.....
#.....
print (h1_elem)
print (a_elem)
print (a_elem)

p_elements = driver.find_elements(By.XPATH, "//p1")
p_elements
print (p_elements)


elem = None
if p_elements:
    elem = p_elements[0]
else:
    print("Element not found")

print(elem)

############################################
#Different Approach with WebDriverWait
############################################

driver.get("https://www.example.com")
selector = (By.XPATH, "//h1")
wait = WebDriverWait(driver, 10)
h1_elem = wait.until(EC.presence_of_element_located(selector))

selector = (By.XPATH, "//a")
wait = WebDriverWait(driver, 10)
a_elem = wait.until(EC.presence_of_element_located(selector))

selector = (By.XPATH, "//p")
wait = WebDriverWait(driver, 10)
p_elem = wait.until(EC.presence_of_element_located(selector))

selector = (By.XPATH, "//p")
wait = WebDriverWait(driver, 10)
p_elements = wait.until(EC.presence_of_all_elements_located(selector))

print(p_elements)
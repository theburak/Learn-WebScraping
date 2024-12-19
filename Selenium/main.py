################
# Main  (This file is only for initializing driver)
# (Please refer to other .py files for lecture codes)
################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Initialize Driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://example.com/")

print (driver.title)
print (driver.current_url)

#driver.quit() # Commented out to keep the browser open
time.sleep(5) # Let the user actually see something!
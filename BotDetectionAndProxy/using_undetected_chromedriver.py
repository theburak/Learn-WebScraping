######################################################
# Using undetected-chromedriver to Pass Bot Tests
######################################################
import undetected_chromedriver as uc
# pip install undetected_chromedriver
from selenium import webdriver

url = "https://bot.sannysoft.com"

driver = uc.Chrome()
with driver:
    driver.get(url)
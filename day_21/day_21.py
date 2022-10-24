from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Safari()

browser.get('http://www.google.com')
time.sleep(32)

assert 'Google' in browser.title 
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
Browser = Firefox()

link = 'https://www.google.com/'

Browser.get(link)

input_area = Browser.find_element(By.NAME, "q")

input_area.send_keys('Instituto joga junto')

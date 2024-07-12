from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
browser = Firefox()

link = "https://www.google.com/"

browser.get(link)

checkboxes = browser.find_elements(By.ID, "input")

for box in checkboxes:
    print("bah")
    

time.sleep(5)

browser.quit()

i = 0
while i < 10:
    i += 1







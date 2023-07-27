from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://google.com")
path = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
search_bar=browser.find_elements_by_xpath(Path1)
search_bar[0].send_keys("India’s new railways project picks up speed")
search_bar[0].send_keys(Keys.ENTER)
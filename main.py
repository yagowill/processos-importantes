import time
from selenium.webdriver.common.by import By
from browser import browser
from find_process import find_process
from login import login
from wait_element import wait_element

browser = browser()


url = "https://www.sistemas.pa.gov.br"

login(browser,url)

browser.get(f"{url}/eprotocolo")

element = wait_element(browser, By.XPATH, '//*[@id="iconmenu_vert:j_id103"]')
browser.execute_script("arguments[0].click();", element)
time.sleep(3)

find_process(browser)
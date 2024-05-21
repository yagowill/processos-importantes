from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_element(browser, by, selector):
    return WebDriverWait(browser, timeout=20).until(EC.presence_of_element_located((
        by,
        selector
    )))
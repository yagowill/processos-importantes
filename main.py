from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
url = "https://www.sistemas.pa.gov.br/governodigital/public/main/index.xhtml"
f = open("login.txt", "r")
user = f.readline().strip()
passwd = f.readline().strip()

browser.get("https://www.sistemas.pa.gov.br/governodigital/public/main/index.xhtml")


login_username = browser.find_element(By.ID, "form_login:login_username")
login_username.send_keys(user)

login_password = browser.find_element(By.ID, "form_login:login_password")
login_password.send_keys(passwd)

browser.find_element(By.ID, "form_login:button_login").click()

browser.find_element(By.CSS_SELECTOR, "#form_sistema\:submit_area > div > div:nth-child(1) > div.SistemaGridImage > a").click()
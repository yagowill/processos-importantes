from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
url = "https://www.sistemas.pa.gov.br"
f = open("login.txt", "r")
user = f.readline().strip()
passwd = f.readline().strip()

browser.get(f"{url}/governodigital")


login_username = browser.find_element(By.ID, "form_login:login_username")
login_username.send_keys(user)

login_password = browser.find_element(By.ID, "form_login:login_password")
login_password.send_keys(passwd)

browser.find_element(By.ID, "form_login:button_login").click()

browser.get(f"{url}/eprotocolo")

element = WebDriverWait(browser, timeout=10).until(EC.presence_of_element_located((
    By.CSS_SELECTOR,
    "#iconmenu_vert\\:panelLocalizarProtocoloEletronico"
)))
browser.execute_script("arguments[0].click();", element)
time.sleep(3)


#ano_protocolo = browser.find_element(By.ID, "protocolo_consult_params:ano_protocolo")
sequencial_protocolo = browser.find_element(By.ID, "protocolo_consult_params:sequencial_protocolo")
sequencial_protocolo.send_keys("359894")

btnPesquisar = WebDriverWait(browser, timeout=10).until(EC.presence_of_element_located((
    By.ID,
    "protocolo_consult_params:botaoPesquisar"
)))

browser.execute_script("arguments[0].click();", btnPesquisar)
time.sleep(3)
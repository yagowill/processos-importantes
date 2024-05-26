from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GovernoDigital():
    
    def __init__(self, webdriver: Chrome) -> None:
        self.webdriver = webdriver
        self.url = "https://www.sistemas.pa.gov.br/governodigital"
            
    def login(self):
        credentials = open("login.txt", "r")
        user = credentials.readline().strip()
        passwd = credentials.readline().strip()
        form_user = (By.ID, "form_login:login_username")
        form_paswd = (By.ID, "form_login:login_password")
        form_submit = (By.ID, "form_login:button_login")

        self.webdriver.get(self.url)
        WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(form_user)).send_keys(user)
        WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(form_paswd)).send_keys(passwd)
        WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(form_submit)).click()
        

from selenium.webdriver.common.by import By
from wait_element import wait_element

def login(browser, url):
    f = open("login.txt", "r")
    user = f.readline().strip()
    passwd = f.readline().strip()

    browser.get(f"{url}/governodigital")


    login_username = wait_element(browser, By.ID, "form_login:login_username")
    login_username.send_keys(user)

    login_password = wait_element(browser, By.ID, "form_login:login_password")
    login_password.send_keys(passwd)

    browser.find_element(By.ID, "form_login:button_login").click()
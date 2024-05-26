from selenium.webdriver import Chrome
from Eprotocol import Eprotocol
from GovernoDigital import GovernoDigital
from Spreadsheet import Spreadsheet

webdriver = Chrome()


governo_digital = GovernoDigital(webdriver)
governo_digital.login()
eprotocol = Eprotocol(webdriver)
eprotocol.open()

spreadsheet = Spreadsheet()
spreadsheet.auth()
processes = spreadsheet.read()
result = eprotocol.find_processes(processes)
spreadsheet.update(result)
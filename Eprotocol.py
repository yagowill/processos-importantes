import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Eprotocol():
    def __init__(self, webdriver: Chrome) -> None:
        self.webdriver = webdriver
        self.url = "https://www.sistemas.pa.gov.br/eprotocolo"
        
    def open(self):
        self.webdriver.get(self.url)
        
    def find_processes(self, values):
        protocol_input = (By.XPATH, '//*[@id="protocolo_form_pesq:protocolo"]')
        btnPesquisar = (By.XPATH, '//*[@id="protocolo_form_pesq:botaoPesquisar"]')
        complement = (By.XPATH, '//*[@id="protocolo_form_consulta:dados"]/tbody/tr[9]/td[4]')
        date_last_processing = (By.XPATH, '//*[@id="protocolo_form_consulta:ultimaTram:0:j_id331"]')
        location_last_processing = (By.XPATH, '//*[@id="protocolo_form_consulta:ultimaTram:0:j_id325"]')
        process_list = []
        
        self.webdriver.get("https://www.sistemas.pa.gov.br/eprotocolo/consulta/documento/consulta_protocolo_lista.seam")
        processes = values
        for process in processes:
            protocol_number = process.strip()
            
            field =  WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(protocol_input))
            field.clear()
            field.send_keys(protocol_number)
            
            submit =  WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(btnPesquisar))
            
            self.webdriver.execute_script("arguments[0].click();", submit)
            time.sleep(3)
            
            process_list.append([
                WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(complement)).text,
                 WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(date_last_processing)).text,
                 WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located(location_last_processing)).text.split(" » ")[1]
            ])
        return process_list
                
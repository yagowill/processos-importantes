import time
from wait_element import wait_element
from selenium.webdriver.common.by import By

def find_process(browser):
    processes = open("processos.txt", "r").readlines()
    print("    Processo     | Data Última Tramitação |   Localização Última Tramitação")
    print("-"*78)
    for process in processes:
        protocol_number = process.strip()
        
        protocol_input = wait_element(browser, By.XPATH, '//*[@id="protocolo_form_pesq:protocolo"]')
        protocol_input.clear()
        protocol_input.send_keys(protocol_number)

        btnPesquisar = wait_element(browser, By.XPATH, '//*[@id="protocolo_form_pesq:botaoPesquisar"]')

        browser.execute_script("arguments[0].click();", btnPesquisar)
        time.sleep(3)
        
        date_last_processing = wait_element(
            browser,
            By.XPATH,
            '//*[@id="protocolo_form_consulta:ultimaTram:0:j_id331"]'
        ).text

        location_last_processing = wait_element(
            browser,
            By.XPATH,
            '//*[@id="protocolo_form_consulta:ultimaTram:0:j_id325"]'
        ).text
        
        print(f"    {protocol_number}    |      {date_last_processing}     |    {location_last_processing.split('»')[1].strip()}   ")
        print("-"*78)

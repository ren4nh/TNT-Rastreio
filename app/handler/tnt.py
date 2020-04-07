# -*- encoding: utf-8 -*-

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import json

class TntHandler:

    def scrap(self, data):
        # Grab content from URL (Pegar conteúdo HTML a partir da URL)
        url = "https://radar.tntbrasil.com.br/radar/public/localizacaoSimplificada"

        option = Options()
        option.headless = True
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=option)

        try:
            driver.get(url)
            driver.implicitly_wait(5)  # in seconds

            results = []

            select = Select(driver.find_element_by_id("remDest"))
            select.select_by_value("D")

            element = driver.find_element_by_id("nrIdentificacao")
            element.send_keys(data['identificacao'])

            select = Select(driver.find_element_by_id("tpDocumento"))
            select.select_by_value(data['tipodoc'])

            element = driver.find_element_by_id("nrDocumento")
            element.send_keys(data['numdoc'])

            driver.find_element_by_id("buscar").click()

            elements = driver.find_elements_by_class_name("dataTables_empty")

            if len(elements) > 0:
                raise Exception("Nenhum registro encontrado")

            driver.find_element_by_id("results").find_element_by_tag_name("a").click()

            rows = driver.find_elements_by_xpath("//*[@id='occurrences']/tbody/tr")

            for row in rows:
                colums = row.find_elements_by_tag_name("td")
                results.append({'data': colums[0].text, 'ocorrencia': colums[1].text, 'filial': colums[2].text})
            
            return json.dumps(results, ensure_ascii=False).encode('utf8')

        except Exception as identifier:
            print(identifier)
            return { 'error' : str(identifier)}
        finally:
            driver.quit()

# -*- encoding: utf-8 -*-

import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from app.email import send_email
from app.utils import utils


class TntHandler:

    def __init__(self):
        self.option = Options()
        self.option.headless = True
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.implicitly_wait(5)  # in seconds
        self.url = "https://radar.tntbrasil.com.br/radar/public/localizacaoSimplificada"

    def scrap(self, data):      
        try:
            driver = self.driver
            driver.get(self.url)
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
                raise Exception("No records found")

            driver.find_element_by_id("results").find_element_by_tag_name("a").click()

            rows = driver.find_elements_by_xpath("//*[@id='occurrences']/tbody/tr")

            for row in rows:
                colums = row.find_elements_by_tag_name("td")
                results.append({'data': colums[0].text, 'ocorrencia': colums[1].text, 'filial': colums[2].text})
            
            send_email("Rastreio TNT", "tracking@hartwig.com", [data["email"]], None, utils.convert_to_html(results))
            
            return { 'success' : 'Please check your email to get the result'}

        except Exception as identifier:
            print(identifier)
            return { 'error' : str(identifier)}
        finally:
            self.driver.quit()
        
        

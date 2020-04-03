# -*- encoding: utf-8 -*-

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import json

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://radar.tntbrasil.com.br/radar/public/localizacaoSimplificada"

identificacao = input("Informe o CNPJ/CPF:")
tipo_doc = input("Informe o tipo de documento (NF - Nota fiscal, CTRC - Doc. Serviço, RCLI - Ref. Cliente):")
num_doc = input("Informe o numero do documento:")

option = Options()
option.headless = False
driver = webdriver.Chrome(options=option)

try:
    driver.get(url)
    driver.implicitly_wait(10)  # in seconds
    wait = WebDriverWait(driver, 10)

    results = []


    select = Select(driver.find_element_by_id("remDest"))
    select.select_by_value("D")

    element = driver.find_element_by_id("nrIdentificacao")
    element.send_keys(identificacao)

    select = Select(driver.find_element_by_id("tpDocumento"))
    select.select_by_value(tipo_doc)

    element = driver.find_element_by_id("nrDocumento")
    element.send_keys(num_doc)

    driver.find_element_by_id("buscar").click()

    elements = driver.find_elements_by_class_name("dataTables_empty")

    if len(elements) > 0:
        raise Exception("Nenhum registro encontrado")

    driver.find_element_by_id("results").find_element_by_tag_name("a").click()

    rows = driver.find_elements_by_xpath("//*[@id='occurrences']/tbody/tr")

    for row in rows:
        colums = row.find_elements_by_tag_name("td")
        results.append({'data': colums[0].text, 'ocorrencia': colums[1].text, 'filial': colums[2].text})
    
    print(results)


except Exception as identifier:
    print(identifier)
finally:
    driver.quit()






# # Dump and Save to JSON file (Converter e salvar em um arquivo JSON)
# with open('ranking.json', 'w', encoding='utf-8') as jp:
#     js = json.dumps(top10ranking, indent=4)
#     jp.write(js)
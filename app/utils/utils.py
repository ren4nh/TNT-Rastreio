# -*- coding: utf-8 -*-

# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def page_has_loaded(self):
    print("Checking if {} page is loaded.".format(self.current_url))
    page_state = self.execute_script('return document.readyState;')
    return page_state == 'complete'

# def wait_reload(self, wait):
#     # wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR("div[class*='ui-overlay-visible']")))
#     # wait.until(EC.invisibility_of_element_located(By.CSS_SELECTOR("div[class*='ui-overlay-visible']")))

def convert_to_html(results):
    html = '<html><head></head><body><p>Hello, check the tracking results below</p><table border="1"><thead></thead><tbody><tr><td>Date</td><td>Issue</td><td>Branch</td></tr>'
    for result in results:
        html +='<tr><td>' + result['data'] + "</td><td>" + result['ocorrencia'] + "</td><td>" + result['filial'] + "</td></td>"
    html += "</tbody></table></body></html>"
    return html
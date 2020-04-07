from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def page_has_loaded(self):
    print("Checking if {} page is loaded.".format(self.current_url))
    page_state = self.execute_script('return document.readyState;')
    return page_state == 'complete'

def wait_reload(self, wait):
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR("div[class*='ui-overlay-visible']")))
    wait.until(EC.invisibility_of_element_located(By.CSS_SELECTOR("div[class*='ui-overlay-visible']")))
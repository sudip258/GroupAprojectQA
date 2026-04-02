from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locator.Locator import locate

class Searchpage:
    def __init__(self,driver):
        self.driver=driver
        self.lc=locate()

    def search_function(self,search_input):
        search=self.driver.find_element(By.XPATH,self.lc.search_xpath)
        search.click()
        search.send_keys(search_input)
        search.send_keys(Keys.ENTER)
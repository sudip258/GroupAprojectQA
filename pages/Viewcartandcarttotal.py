import time

from locator.Locator import locate
from selenium.webdriver.common.by import By

class Viewcartandcarttotalpage:
    def __init__(self,driver):
        self.driver=driver
        self.lc=locate()

    def view_function(self):
        time.sleep(3)
        continueshopping=self.driver.find_element(By.XPATH,self.lc.continueshopping_xpath)
        time.sleep(3)
        continueshopping.click()
        time.sleep(3)
        cart=self.driver.find_element(By.XPATH,self.lc.cart_xpath)
        time.sleep(3)
        cart.click()



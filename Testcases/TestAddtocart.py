from locator.Locator import locate
from selenium.webdriver.common.by import By
import time
class Addtocartpage:
    def __init__(self,driver):
        self.driver=driver
        self.lc=locate()

    def addtocart_function(self):
        hummingbird_printed_t_shirt=self.driver.find_element(By.XPATH,self.lc.hummingbird_xpath)
        hummingbird_printed_t_shirt.click()
        add_to_cart=self.driver.find_element(By.XPATH,self.lc.addtocart_xpath)
        add_to_cart.click()
        time.sleep(3)
        proceed_to_checkout=self.driver.find_element(By.XPATH,self.lc.proceedtocheckout_xpath)
        proceed_to_checkout.click()
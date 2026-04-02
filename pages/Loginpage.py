from locator.Locator import locate
from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.lc=locate()


    def loginfunction(self,email_input,password_input):
        signup=self.driver.find_element(By.XPATH,self.lc.sign_in_xpath)
        signup.click()
        email=self.driver.find_element(By.XPATH,self.lc.email_xpath)
        email.click()
        email.send_keys(email_input)
        password=self.driver.find_element(By.XPATH,self.lc.password_xpath)
        password.click()
        password.send_keys(password_input)
        login_button=self.driver.find_element(By.XPATH,self.lc.login_button_xpath)
        login_button.click()





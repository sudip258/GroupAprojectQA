import time
import unittest
import selenium
from pages.Loginpage import Loginpage
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.Addtocartpage import Addtocartpage
from pages.Viewcartandcarttotalpage import Viewcartandcarttotalpage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qap.bishalkarki.com/")
        self.lp = Loginpage(self.driver)
        self.lp.loginfunction("roronoa98619@gmail.com", "Ujjwalqwerty")
        hummingbird_printed_sweater = self.driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/section/section/section[1]/div/div[2]/article/div/div[1]/a/picture/img')
        hummingbird_printed_sweater.click()
        add_to_cart = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button')
        add_to_cart.click()

        self.vc=Viewcartandcarttotalpage(self.driver)


    def test_name(self):
        try:

            self.vc.view_function()

            expected="Hummingbird printed sweater"

            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/div/div[1]/div/div[2]/ul/li/div/div[2]/div[1]/a').text

            self.assertEqual(expected,actual,'Failed to view cart')
        except Exception as e:
            self.fail("Failed to view cart")


    def test_price(self):
        try:
            self.vc.view_function()
            expected="$28.72"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[2]/div/div[2]/span/strong').text
            self.assertEqual(expected,actual,"Price not same")
        except Exception as e:
            self.fail("Price not same")

    def test_total(self):
        try:
            self.vc.view_function()
            expected="$28.72"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/div/div[2]/div[1]/div[1]/div[2]/div[2]/span[2]').text
            self.assertEqual(expected,actual,"Total not same")
        except Exception as e:
            self.fail("Total not same")





    def tearDown(self):
       self.driver.quit()











if __name__ == '__main__':
    unittest.main()

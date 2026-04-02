import unittest
import pages.Loginpage as Loginpage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class MyTestCase(unittest.TestCase,):


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qap.bishalkarki.com/")
        self.lp=Loginpage.Loginpage(self.driver)

    def test_login(self):
        try:
            self.lp.loginfunction("roronoa98619@gmail.com","Ujjwalqwerty")
            time.sleep(5)
            expected="Ujjwal Prajapati"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a[2]/span').text
            self.assertEqual(expected,actual,"Login Failed")
        except Exception as e:
            self.fail('Error:',str(e))

    def test_login1(self):
        try:
            self.lp.loginfunction("roronoa98619@gmail.com","ujjwalpoosop")
            time.sleep(5)
            expected="Authentication failed."
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/div/section/div/ul/li').text
            self.assertEqual(expected,actual,"Login Failed")
        except Exception as e:
            self.fail('Error:',str(e))

    def test_login2(self):
        try:
            self.lp.loginfunction("roronoa9@gmail.com","Ujjwalqwerty")
            time.sleep(5)
            expected="Authentication failed."
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/div/section/div/ul/li').text
            self.assertEqual(expected,actual,"Login Failed")
        except Exception as e:
            self.fail('Error:',str(e))

    def test_login3(self):
        try:
            self.lp.loginfunction("","")
            time.sleep(5)
            expected="Log in to your account"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/header/h1').text
            self.assertEqual(expected,actual,"Login Failed")
        except Exception as e:
            self.fail('Error:',str(e))

    def test_login4(self):
        try:
            self.lp.loginfunction("roronoa98619@gmail.com","")
            time.sleep(5)
            expected="Log in to your account"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/header/h1').text
            self.assertEqual(expected,actual,"Login Failed")
        except Exception as e:
            self.fail('Error:',str(e))
    def test_login5(self):
        try:
            self.lp.loginfunction("","Ujjwalqwerty")
            time.sleep(5)
            expected="Log in to your account"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/header/h1').text
            self.assertEqual(expected,actual,"Login Failed")
        except Exception as e:
            self.fail('Error:',str(e))




    def tearDown(self):
        time.sleep(3)
        self.driver.quit()







if __name__ == '__main__':
    unittest.main()


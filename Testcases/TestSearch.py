import unittest



import pages.Loginpage as Loginpage
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

from pages.Searchpage import Searchpage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qap.bishalkarki.com/")
        self.lp = Loginpage.Loginpage(self.driver)
        self.lp.loginfunction("deeyagautam55@gmail.com", "diya@321#")
        self.search=Searchpage(self.driver)

    def test_search1(self):
        try:
            self.search.search_function("Hummingbird printed sweater")
            time.sleep(5)
            expected="Hummingbird Printed Sweater"
            actual=self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/div[3]/div[1]/div/article/div/div[2]/h2/a').text
            self.assertEqual(expected,actual,"Search Failed")
        except Exception as e:
            self.fail('Error:',str(e))

    def test_search2(self):
        try:
            self.search.search_function("")
            time.sleep(5)
            expected = "No matches were found for your search"
            actual = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/div[2]/section/h4').text
            self.assertEqual(expected, actual, "Search Failed")
        except Exception as e:
            self.fail('Error:', str(e))

    def test_search3(self):
        try:
            self.search.search_function("Playstation 5")
            time.sleep(5)
            expected = "No matches were found for your search"
            actual = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/div[2]/section/h4').text
            self.assertEqual(expected, actual, "Search Failed")
        except Exception as e:
            self.fail('Error:', str(e))

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()

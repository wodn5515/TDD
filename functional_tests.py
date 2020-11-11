from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/killcoding/desktop/chromedriver/chromedriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No resuelts found.", driver.page_source)

    def test_dcjeil_title(self):
        driver = self.driver
        driver.get("http://dcjeil.net")
        self.assertIn("덕천", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
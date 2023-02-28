import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#This test case will use selenium, a library that automates webpages.
class TestSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()#Starts test window.
        
    def tearDown(self):
        self.driver.quit() #quits out the test window
    def test_title(self):
        self.driver.get("0.0.0.127")
        self.assertEqual(self.driver.title, "")
        #Is the server up and running?
    def test_search(self):
        self.driver.get("http://www.example.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("example search")
        search_box.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", self.driver.page_source)
#Can we find the site while runnning given search criteria
if __name__ == '__main__':
    unittest.main()
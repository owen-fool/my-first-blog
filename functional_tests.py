from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_is_it_blog(self):
       
        self.assertIn('Blog', self.browser.title)
        #self.fail('Finish the test!')

    def test_click_to_CV(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/a[1]/span").click()

if __name__ == '__main__':
    unittest.main()

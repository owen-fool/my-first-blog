from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 20


class NewVisitorTest(LiveServerTestCase):

    def wait_for_CV_page(self):
        start_time = time.time()
        while True:
            try:
                showing = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/h2").text
                
                self.assertIn('CV', showing)
                return
            except (AssertionError, WebDriverException) as e:
                
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def test_is_it_blog(self):
       
        self.assertIn('Blog', self.browser.title)
        #self.fail('Finish the test!')

    def test_click_to_CV(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/a[1]/span").click()
        self.wait_for_CV_page()

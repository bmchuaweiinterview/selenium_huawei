from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest
from selenium.webdriver.common.keys import Keys
import logging
import HtmlTestRunner
import re

class amazonNikon(unittest.TestCase):
    def setUp(self):
        #self.log = logging.getLogger('simpleExample')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler_info = logging.FileHandler('info_log.txt')
        handler_info.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler_info.setFormatter(formatter)
        self.logger.addHandler(handler_info)

        self.driver = webdriver.Chrome()
        main_url='https://www.amazon.com'
        self.driver.get(main_url)

        ## Define Amazon page ids here
        self.main_page_search_box='twotabsearchtextbox'

        ## Define xpaths
        self.Product_Title_Xpath='//*[@id="productTitle"]'
        self.results_page_header_xpath="/html/body/div[1]/div[1]/span/h1/div/div[1]/div/div"
        self.Sort_By_Drop_down_Xpath='/html/body/div[1]/div[1]/span/h1/div/div[2]/div/div/span/form/span/span/span/span/span[2]'
        self.Sort_HighLow_Xpath='//*[@id="s-result-sort-select_2"]'
        self.Second_Nikon_item_Xpath='/html/body/div[1]/div[1]/div[1]/div[2]/div/span[3]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/h2/a/span'
        self.Product_Title_Xpath='//*[@id="productTitle"]'
        self.results_page_header_xpath="/html/body/div[1]/div[1]/span/h1/div/div[1]/div/div"


    def tearDown(self):
        self.driver.quit()

    def chrome_nikonAmazon(self):
        self.logger.info(
            '1. Enter the initial amount in the from currency.')
        main_page_search_box=self.driver.find_element_by_id('twotabsearchtextbox')
        main_page_search_box.send_keys('Nikon')
        main_page_search_box.send_keys(Keys.ENTER)

        self.logger.info(
            '2. Check that the user is brought to the results page.')
        results_page_header=self.driver.find_element_by_xpath(self.results_page_header_xpath)
        self.logger.info(results_page_header.text)
        self.assertTrue(re.match('1-16 of over', results_page_header.text))
        self.assertTrue('https://www.amazon.com/s?k=Nikon&ref=nb_sb_noss' in self.driver.current_url)

        self.logger.info(
            '3. Sort results by price, high to low.')
        Sort_Dropdown=self.driver.find_element_by_xpath(self.Sort_By_Drop_down_Xpath)
        Sort_Dropdown.click()

        HighLow_price=self.driver.find_element_by_xpath(self.Sort_HighLow_Xpath)
        HighLow_price.click()

        self.logger.info(
            '4. Enter second result.')
        Second_Nikon_item_link=self.driver.find_element_by_xpath(self.Second_Nikon_item_Xpath)
        Second_Nikon_item_link.click()

        self.logger.info(
            '5. Verify second most expensive result.')
        self.assertTrue('Nikon D5 DSLR' in self.driver.find_element_by_xpath(self.Product_Title_Xpath).text)

    def test_main(self):
        self.chrome_nikonAmazon()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())  

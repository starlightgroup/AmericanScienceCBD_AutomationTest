from time import sleep
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from slack_utilities import post_message_slack


class PromoFlowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        firefox_options = FFOptions()
        # firefox_options.add_argument('--headless')
        cls.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe', options=firefox_options)
        cls.driver.implicitly_wait(30)
        cls.driver.set_page_load_timeout(30)

    def test_promo_flow(self):
        # TEST 1: test to check if promo page loads correctly
        url = 'https://americansciencecbd.com/promo'
        self.driver.get(url)
        sleep(5)
        self.assertEqual(self.driver.current_url, 'https://americansciencecbd.com/promo/desktop?',
                         'Promo Page URL is wrong - {}'.format(self.driver.current_url))
        self.assertTrue(self.is_element_present(By.NAME, 'FirstName', check_for_visibility=True))
        self.assertTrue(self.is_element_present(By.XPATH, '//button[@id="rush-my-order-form-click"]', True))

        # TEST 2: Shipping Page Submit
        self.driver.find_element_by_name('FirstName').send_keys('fname')
        self.driver.find_element_by_name('LastName').send_keys('lname')
        self.driver.find_element_by_name('Address1').send_keys('address line 1')
        self.driver.find_element_by_name('Address2').send_keys('address line 2')
        self.driver.find_element_by_name('City').send_keys('New York')
        Select(self.driver.find_element_by_name('State')).select_by_visible_text('New York')
        self.driver.find_element_by_name('ZipCode').send_keys('10119')
        self.driver.find_element_by_name('Phone').send_keys('9999911111')
        self.driver.find_element_by_name('Email').send_keys('abc@abc.com')
        self.driver.find_element_by_xpath('//button[@id="rush-my-order-form-click"]').click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'cardNumber')))
        self.assertEqual(self.driver.current_url, 'https://americansciencecbd.com/promo/desktop/checkout?',
                         'Checkout Page URL is wrong - {}'.format(self.driver.current_url))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what, check_for_visibility=False):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            elem = self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        if check_for_visibility:
            return elem.is_displayed()
        return True


if __name__ == '__main__':
    outfile = r'E:\PyCharm\Workspace\StarlightGroup\AmericanScienceCBD_AutomationTest\Reports\logfile.txt'
    f = open(outfile, "w")
    f.write('Test Executed On *Windows 10* + *Firefox*')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner, exit=False)
    f.close()
    with open(outfile, 'r') as f:
        post_message_slack(f.read())

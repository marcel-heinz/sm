from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check website
        self.browser.get('http://localhost:8000')

        # notice webiste 'SkinMate'
        self.assertIn('SkinMate', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Check UV', header_text)

        # notice field to enter city name
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter City Name')

        # type "Schwerin" into text box
        inputbox.send_keys('Schwerin')

        # hit enter, the page updates and shows the current uv index
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == "Schwerin" for row in rows),
                        f'New City Not In Table. Content is {table.text}')

        # generate unique url to rember city

        # re-vist site and uv index is still there for "Schwerin"

        # end
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

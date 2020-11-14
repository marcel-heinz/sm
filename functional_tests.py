from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #check website
        self.browser.get('http://localhost:8000')

        #notice webiste 'SkinMate'
        self.assertIn('SkinMate',self.browser.title)

        self.fail('Finish the test')

        #notice field to enter city name

        #type "Schwerin" into text box

        #hit enter, the page updates and shows the current uv index

        #generate unique url to rember city

        #re-vist site and uv index is still there for "Schwerin"

        #end

if __name__ == '__main__':
    unittest.main(warnings='ignore')
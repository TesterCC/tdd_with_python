#!/usr/bin/env python
# coding:utf-8
# python 3.5.2 , django 1.8
# P14


from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    # If setUp throw Exception, tearDown method will not run.
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lily heard there is a application website
        # She visit the homepage
        self.browser.get('http://localhost:8000')

        # User noticed the web title include word "To-Do"
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 应用邀请她输入一个待办事项


if __name__ == '__main__':     # python use it to check whether the script run in command line.
    # unittest.main(warnings='ignore')
    # can delete warnings = 'ignore'(forbidden throw Resource Warning Exception) and try run it.
    unittest.main()    # can delete warnings = 'ignore' and try run it.


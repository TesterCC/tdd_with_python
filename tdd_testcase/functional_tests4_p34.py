#!/usr/bin/env python
# coding:utf-8
# python 3.5.2 , django 1.8
# P34


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框中输入了"Buy peacock feathers"
        # 伊迪丝的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后，页面更新了
        # 待办事项表格中显示了"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table."
        )

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了"Use peacock feathers to make a fly"
        # 伊迪丝做事很有条理
        self.fail('Finish the test!')

        # 页面再次更新，她的清单中显示了这两个待办事项


if __name__ == '__main__':     # python use it to check whether the script run in command line.
    # unittest.main(warnings='ignore')
    # can delete warnings = 'ignore'(forbidden throw Resource Warning Exception) and try run it.
    unittest.main()    # can delete warnings = 'ignore' and try run it.


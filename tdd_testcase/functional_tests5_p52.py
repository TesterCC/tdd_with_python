#!/usr/bin/env python
# coding:utf-8
# python 3.5.2 , django 1.8
# P52


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


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

        # for debug
        time.sleep(5)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        # complex one
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table. -- its text was:\n%s" % (table.text)
        # )

        # simple one
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了"Use peacock feathers to make a fly"
        # 伊迪丝做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，她的清单中显示了这两个待办事项
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 页面中有一些文字解说这个功能

        # 她访问那个URL，发现待办事项清单还在


        # 期望的失败
        self.fail('Finish the test!')


if __name__ == '__main__':     # python use it to check whether the script run in command line.
    # unittest.main(warnings='ignore')
    # can delete warnings = 'ignore'(forbidden throw Resource Warning Exception) and try run it.
    unittest.main()    # can delete warnings = 'ignore' and try run it.


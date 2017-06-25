#!/usr/bin/env python
# coding=utf-8

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

# class SmokeTest(TestCase):
    # def test_bad_maths(self):
    #     self.assertEqual(1+1, 3)   # expected failed


# python manage.py test lists.tests.HomePageTest.test_xxx    # run specific testcase
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)  # .decode() 把response.content中的字节转换成Python中的,Unicode字符串
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))   # Didn't add .strip() works also well.

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'     # 传入数据

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html',
                                         {'new_item_text': 'A new list item'}
                                         )
        self.assertEqual(response.content.decode(), expected_html)


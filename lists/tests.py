#!/usr/bin/env python
# coding=utf-8

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

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
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))




#!/usr/bin/env python
# coding:utf-8
# python 3.5.2 , django 1.8
# P4-5


from selenium import webdriver


browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

browser.quit()    # if assert pass, close browser

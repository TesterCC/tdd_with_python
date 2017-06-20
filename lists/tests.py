#!/usr/bin/env python
# coding=utf-8

from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)   # expected failed



# -*- coding: utf-8 -*-
import unittest

import requests


class TestHttpApi(unittest.TestCase):
    def test_get_user_feedback(self):
        response = requests.get('http://127.0.0.1:8686/feedbacks/user', params={
            'offset': 0,
            'limit': 10
        })
        print(response.text)

if __name__ == '__main__':
    unittest.TestCase()
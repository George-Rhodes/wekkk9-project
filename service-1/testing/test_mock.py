from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from requests.api import request
import requests
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    

    def test_lottopage_view(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


    def test_postlotto_view(self):

        with patch('requests.get') as g:
            with patch('requests.post') as p:

                g.return_value.text = 'AA'
                p.return_value.text = 'sorry, you win nothing'
                response = self.client.get(url_for('lotto'))
                self.assertEqual(response.status_code, 200)
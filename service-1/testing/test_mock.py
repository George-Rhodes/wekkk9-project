from flask import url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from unittest.mock import patch
from requests.api import request
import requests
import unittest
import requests_mock
from application.models import ticks
from application import app,db

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        return app
    
    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestResponse(TestBase):
    

    def test_lottopage_view(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


    def test_postlotto_view(self):
        with self.client:
            with requests_mock.Mocker() as m:
                m.get('http://service-2:5001/alpha', text='KK')
                m.get('http://service-3:5002/number', text= '23')
                m.post('http://service-3:5002/number', text= 'death')
                response = self.client.get(url_for('lotto'),follow_redirects=True)
                self.assertEqual(response.status_code, 200)


      #  with patch('requests.get') as g:
       #     with patch('requests.post') as p:

            #    g.return_value.text = 'AA'
            #    p.return_value.text = 'sorry, you win nothing'
            #    response = self.client.get(url_for('lotto'))
            #   self.assertEqual(response.status_code, 200)
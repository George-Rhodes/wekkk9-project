from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestAlpha(TestBase):
    def test_alpha(self):
        response = self.client.get(url_for('alpha'))
        self.assertEquals(response.status_code,200)
from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
        return app

class Testprizes(TestBase):
    def test_death_prize(self):
        response = self.client.post(
            url_for('prize'),
            data="KK12",
            follow_redirects=True
        )
        self.assertIn(b"Death", response.data)
    


    def test_limb_prize(self):
        response = self.client.post(
            url_for('prize'),
            data="LK67",
            follow_redirects=True
        )
        self.assertIn(b"lose a limb", response.data)

    def test_great_prize(self):
        response = self.client.post(
            url_for('prize'),
            data="GG90",
            follow_redirects=True
        )
        self.assertIn(b"you have won a life time supply of money , trip to the Bahamas, and your own private island. Our agent will contact you shortly, dont worry we know where you live", response.data)
    
    def test_okay_prize(self):
        response = self.client.post(
            url_for('prize'),
            data="GL89",
            follow_redirects=True
        )
        self.assertIn(b"You have won a tenner", response.data)
    
    def test_no_prize(self):
        response = self.client.post(
            url_for('prize'),
            data="SJ78",
            follow_redirects=True
        )
        self.assertIn(b"sorry, you win nothing", response.data)
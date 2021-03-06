from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from uvindex.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'city_text': 'A new city'})
        self.assertIn('A new city', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

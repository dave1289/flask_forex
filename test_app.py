from unittest import TestCase
from app import app
from flask import session

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ForexConverter(TestCase):

   def test_home(self):
      with app.test_client() as client:
         res = client.get('/')
         html = res.get_data(as_text=True)

         self.assertEqual(res.status_code, 200)
         self.assertIn('<h1 class="text-center display-3">Forex Converter</h1>', html)

   def test_convert(self):
      with app.test_client() as client:
         res = client.get('/convert', follow_redirects=True)
         html = res.get_data(as_text=True)

         self.assertEqual(res.status_code, 405)

         
from django.test import TestCase
import os
from django.contrib.auth.password_validation import validate_password


# import the settings.py
#from django.conf import settings

class InventorySystemTest(TestCase):

    def test_secret_key_strength(self):
        #  settings.SECRET_KEY ( get the whole of setting.py page)

        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

        # testing if the SECRET_KEY is strong with the validate_password method
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak Secret key {e}'
            self.fail(msg)
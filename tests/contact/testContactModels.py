from django.test import TestCase, SimpleTestCase
from contact.models import ContactForm
from datetime import datetime, timedelta
from payments.models import User

class UserModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_user = User(email = "j@j.com", name = 'test user')
        cls.test_user.save()
		
    def test_contactform_str_returns_email(self):
        self.assertEqual(str(self.test_user), "j@j.com")
        
    def test_ordering(self):
        self.assertEquals(User.get_by_id(1), self.test_user)
		
from decimal import Decimal

from django.test import TestCase

from peacecorps.admin import StrictUserCreationForm, StrictAdminPasswordChangeForm


class StrictUserCreationTest(TestCase):
    def test_blank(self):
        """ Check to ensure the password cannot be blank."""
        form_data = {
            'username': 'testuser',
            'password1': '',
            'password2': ''
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_uppercase(self):
        """ Check to ensure the password contains an uppercase letter."""
        form_data = {
            'username': 'testuser',
            'password1': 'q*9x=^2hg&v7u?u9tg?u',
            'password2': 'q*9x=^2hg&v7u?u9tg?u'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_lowercase(self):
        """ Check to ensure the password contains a lowercase letter."""
        form_data = {
            'username': 'testuser',
            'password1': 'A=R7-%=K?K@B^!9Q8=C+',
            'password2': 'A=R7-%=K?K@B^!9Q8=C+'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_number(self):
        """ Check to ensure the password contains a number."""
        form_data = {
            'username': 'testuser',
            'password1': 'CDr=cpz&Z&a!cuP-nAQe',
            'password2': 'CDr=cpz&Z&a!cuP-nAQe'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_specialchar(self):
        """ Check to ensure the password contains a special character."""
        form_data = {
            'username': 'testuser',
            'password1': 'vNzwXpzKJyTshvHsuULn',
            'password2': 'vNzwXpzKJyTshvHsuULn'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_length(self):
        """ Check to ensure the password is 20 characters long."""
        form_data = {
            'username': 'testuser',
            'password1': 'c897B$eH@',
            'password2': 'c897B$eH@'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

class StrictAdminPasswordChangeFormTest(TestCase):
    def test_blank(self):
        """ Check to ensure the password cannot be blank."""
        form_data = {
            'password1': '',
            'password2': ''
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_uppercase(self):
        """ Check to ensure the password contains an uppercase letter."""
        form_data = {
            'password1': 'q*9x=^2hg&v7u?u9tg?u',
            'password2': 'q*9x=^2hg&v7u?u9tg?u'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_lowercase(self):
        """ Check to ensure the password contains a lowercase letter."""
        form_data = {
            'password1': 'A=R7-%=K?K@B^!9Q8=C+',
            'password2': 'A=R7-%=K?K@B^!9Q8=C+'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_number(self):
        """ Check to ensure the password contains a number."""
        form_data = {
            'password1': 'CDr=cpz&Z&a!cuP-nAQe',
            'password2': 'CDr=cpz&Z&a!cuP-nAQe'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_specialchar(self):
        """ Check to ensure the password contains a special character."""
        form_data = {
            'password1': 'vNzwXpzKJyTshvHsuULn',
            'password2': 'vNzwXpzKJyTshvHsuULn'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_length(self):
        """ Check to ensure the password is 20 characters long."""
        form_data = {
            'password1': 'c897B$eH@',
            'password2': 'c897B$eH@'
        }
        form = StrictUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
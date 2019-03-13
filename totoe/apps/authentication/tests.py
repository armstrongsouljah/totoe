from django.test import TestCase
from .models import User

class TestUserModel(TestCase):
    def setUp(self):
        self.model = User()

    def test_creating_user_without_email_fails(self):
        with self.assertRaises(Exception) as context:
            User.objects.create_user(
                '',
                'johndoe',
                'password123'
            )
            self.assertTrue('Email must not be blank' in context.exception)

    def test_creating_user_without_username_fails(self):
        with self.assertRaises(Exception) as context:
            User.objects.create_user(
                'john@doe.com',
                '',
                'password123'
            )
            self.assertTrue('Username must not be blank' in context.exception)

    def test_creating_user_without_password_fails(self):
        with self.assertRaises(Exception) as context:
            User.objects.create_user(
                'john@doe.com',
                'johndoe',
                ''
            )
            self.assertTrue('Username must not be blank' in context.exception)

    def test_creating_a_user_with_valid_data_succeeds(self):
        User.objects.create_user(
                'john@doe.com',
                'johndoe',
                'password123'
            )
        self.assertEqual(User.objects.count(), 1)

    def test_createstaff_user_with_valid_data_succeeds(self):
        User.objects.create_staffuser('johndoe@email.com', 'johndoe', 'password123')
        self.assertEqual(User.objects.first().is_staff, True)

    def test_model_represents_instance_correctly(self):
        User.objects.create_staffuser('johndoe@email.com', 'johndoe', 'password123')
        self.assertEqual(str(User.objects.first()), User.objects.first().email)


    def test_create_staff_user_without_password_fails(self):
        with self.assertRaises(Exception) as context:
            User.objects.create_staffuser('johndoe@email.com', 'johndoe')
            self.assertTrue('Staff users must have a password' in context.exception)

    def test_createsuper_user_with_valid_data_succeeds(self):
        User.objects.create_superuser('johndoe@email.com', 'johndoe', 'password123')
        self.assertEqual(User.objects.first().is_active, True)
        self.assertEqual(User.objects.first().is_superuser, True)

    def test_create_super_user_without_password_fails(self):
        """ Checks if creating a user without a password fails """
        with self.assertRaises(Exception) as context:
            User.objects.create_superuser('johndoe@email.com', 'johndoe', '')
            self.assertTrue('Super users must have a password' in context.exception)

    def test_get_username_succeeds(self):
        """ Checks if returning the username succeeds """
        User.objects.create_user(
                'john@doe.com',
                'johndoe',
                'password123'
            )
        self.assertEqual(User.objects.first().get_username, 'johndoe')

    def test_get_shortname_succeeds(self):
        """ returns a short name by splitting the email address """
        User.objects.create_user(
                'john@doe.com',
                'johndoe',
                'password123'
            )
        self.assertEqual(User.objects.first().get_short_name, 'john')

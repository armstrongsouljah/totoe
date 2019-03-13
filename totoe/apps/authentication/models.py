from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """ Class for handling user creation operations '"""

    def create_user(self, email, username, password=None):
        """ creates a default user with no admin privileges"""
        if not email:
            raise TypeError("Email must not be blank")
        
        if not username:
            raise TypeError("Username must not be blank")
        
        if not password:
            raise TypeError("Password must not be blank")
        
        user = self.model(
                            username=username, 
                            email=self.normalize_email(email)
                            )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email, username, password=None, admin=False, staff=True):
        """ creates a user with rights to log into the admin site """

        if not password:
            raise TypeError("Staff users must have a password")
        
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.admin= admin
        user.staff = staff
        user.save()
        return user

    def create_superuser(self, email, username, password=None, admin=True, staff=True):
        """Creates a user with admin privileges"""

        if not password:
            raise TypeError("Super users must have a password")
        
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.admin= admin
        user.staff = staff
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    """ Creates a new user instance """

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=125, unique=True)
    password = models.CharField(max_length=254)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.admin
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def get_username(self):
        return self.username
    
    @property
    def get_short_name(self):
        return self.email.split("@")[0]

    


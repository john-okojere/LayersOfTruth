from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from .manager import UserManager


GENDER_CATEGORY=(
    ('Male','Male'),
    ('Female','Female'),
)
ROLE_CATEGORY=(
    ('ADMIN','ADMIN'),
    ('HOD','HOD'),
    ('HOU','HOU'),
    ('WORKER','WORKER'),
    ('USER','USER'),
)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    first_name = models.CharField(verbose_name='first name', max_length=150, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=150, blank=True)
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex],
        max_length=16,
        unique=True,
        help_text="Phone number must be entered in the format: '+999999999'.",
        error_messages={
            'unique': "This Phone has been used already",
        },
        ) # validators should be a list
    email = models.EmailField(verbose_name='email address', unique=True,
        error_messages={
            'unique': "This email has been used already",
        },
    )
    gender = models.CharField(max_length= 20, choices=GENDER_CATEGORY)

    role = models.CharField(max_length= 20, choices=ROLE_CATEGORY)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    update_fields = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone','email']


    objects = UserManager()
    
    
    def save(self,force_insert=True,using='dataset'):
        super().save(force_insert)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username



class OnlineSoul(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    checked = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.phone}'
    


class Prayers(models.Model):
    name = models.CharField(max_length=255)
    request = models.CharField(max_length=255)
    checked = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.request}'
    

class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    checked = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.request}'
    
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser


class User(AbstractBaseUser):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=128, verbose_name='password')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    # This is needed to be able to login with my token with the user database of django
    # Since im using same values that django default username,password to authenticate
    # I need to indicate which will be the user manager to perform al queries to DB
    objects = UserManager()

    class Meta:
        db_table = 'user'
        ordering = ('name',)
        app_label = 'app'

    def __str__(self):
        return self.username

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import dispatcher

from django.contrib.auth.models import AbstractUser #basic django user model

class Teacher(AbstractUser):# overwrites the basic user model. 
    pass
    #we can add any extra feilds here

#still working on this but should eventually makes creat user work for our Teacher usesr
'''
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
'''
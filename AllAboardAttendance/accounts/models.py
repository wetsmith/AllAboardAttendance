from django.db import models
from django.contrib.auth.models import User
from django.dispatch import dispatcher
from django.contrib.auth.models import AbstractUser, BaseUserManager #basic django user model

class UserManager(BaseUserManager):#manages the creation and set up of users both Teacher and Superuser
    use_in_migrations=True
    
    def _create_user(self, email, password, **extra_fields):#general user creation
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)
        teacher = self.model(email=email, **extra_fields)
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

    def create_user(self, email, password=None, **extra_fields):#creates a teacher
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):#creates a superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)    
    
    
class Teacher(AbstractUser):# overwrites the basic user model. 
    username =None#email will be used as our username
    email = models.EmailField( ('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()#sets the magager for teacher as our UserManager
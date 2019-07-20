from django.contrib.auth.models import User
from django.db import models
from django.dispatch import dispatcher

from django.contrib.auth.models import AbstractUser #basic django user model
#from course.models import Course

class Teacher(AbstractUser):# overwrites the basic user model. 
	def __str__(self):
		return self.email
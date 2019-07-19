from django.contrib.auth.models import User
from django.db import models
from django.dispatch import dispatcher

from django.contrib.auth.models import AbstractUser #basic django user model
#from course.models import Course

class Teacher(AbstractUser):# overwrites the basic user model. 
	#course = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
	#we can add any extra feilds here
	def __str__(self):
		return self.email

class CourseList(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courselist")
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
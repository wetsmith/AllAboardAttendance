import datetime
#import lecture

from django.db import models
from django.utils import timezone

#from lecture import models as Lecture

class Course(models.Model):
	pub_date = models.DateTimeField('date published', default = timezone.now())
	course_title = models.CharField(max_length=50)
	#note: lecture model has a foriegn key to here!
	def __str__(self):
		return self.course_title + ": " + str(self.pub_date.year)
	   
class Student(models.Model):
	student_id = models.CharField(max_length=20, default = 'student')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
	def __str__(self):
		return self.student_id
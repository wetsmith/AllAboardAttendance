import datetime

from django.db import models
from django.utils import timezone

from .Lecture.models import Lecture

class Course(models.Model):
    pub_date = models.DateTimeField('date published', default = timezone.now())
    course_title = models.CharField(max_length=50)
    #NEED TO ADD PROPER IMPORTS :D
    lecture = ForeignKey(Lecture, on_delete=models.CASCADE)
    student_ids = ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_title + ": " + str(self.pub_date.year)
       
class Student(models.Model):
    student_id = models.CharField(max_length=20)
    def __str__(self):
        return self.student_id
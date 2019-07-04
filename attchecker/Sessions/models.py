import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Session(models.Model):
    #question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default = timezone.now())
    def __str__(self):
        return str(self.pub_date)
    
    
class Attendent(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student_ID = models.CharField(max_length=20)
	#position: front, middle, back 
    position = models.CharField(max_length=20, default = 'NA')
    #connection: >=2 present, <2 partial, -1 absent
    connections = models.IntegerField(default=-1)
    pub_date = models.DateTimeField('date published', default = timezone.now())
    def __str__(self):
        return self.student_ID + ": " + str(self.connections)
    #function to add student ID to right list?
        
        
class DirEdge(models.Model):
    attendent = models.ForeignKey(Attendent, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date connection made',default = timezone.now())
    directionID = models.CharField(max_length=20)
    def __str__(self): 
        return self.attendent.student_ID + " -> " + self.directionID
    #write function to update # of connections in attendent?

""" If we want to save a list of students, we can, but Matt recommends we just query the data basestring
    We can query a session's list of attendents for connections <=2, >2, or -1 
    
class studentList(models.Model):
    session = models.ForeignKey(Session, on_delete=CASCADE)
    
class student(models.Model):
    student = models.ForeignKey(studentList, on_delete=CASCADE)
    student_ID = models.CharField(max_length=20)
    absent = models.IntegerField(default=0)
    partial = models.IntegerField(default=0)
    present = models.IntegerField(default=0)
    
"""
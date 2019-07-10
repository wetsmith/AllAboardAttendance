import datetime

from django.db import models
from django.utils import timezone


class Lecture(models.Model):
    lecture_title = models.CharField(max_length=20, default = 'default')
    pub_date = models.DateTimeField('date published', default = timezone.now())

    def __str__(self):
        return self.lecture_title + ": " + str(self.pub_date)


class Attendant(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    temp_id = models.CharField(max_length=20, default = "no code")
    position = models.CharField(max_length=20, default='N/A')
    connections = models.IntegerField(default=-1)
    pub_date = models.DateTimeField('date published', default = timezone.now())

    def one_up(self):
        self.connections = self.connections + 1

    def __str__(self):
        return self.student_id + " connections: " + str(self.connections)


class DirEdge(models.Model):
	attendant = models.ForeignKey(Attendant, on_delete=models.CASCADE, null = True)
	pub_date = models.DateTimeField('date connection made', default = timezone.now())
	direction_id = models.CharField(max_length=20)

	def __str__(self):
		return self.attendant.student_id + " -> " + self.direction_id
import datetime


from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Lecture(models.Model):
	lecture_title = models.CharField(max_length=20, default = 'default')
	lecture_key = models.CharField(max_length=20, default = 'default')
	lecture_title_slug = models.SlugField(
		max_length=20, 
		null = True,
		unique = True, 
		editable = False)
	lecture_key_slug = models.SlugField(
		max_length=20, 
		null = True,
		unique = True, 
		editable = False)
	lecture_qr = models.ImageField(
		upload_to = 'qrimages',
		null = True)
	pub_date = models.DateTimeField('date published', default = timezone.now())
	course = models.ForeignKey('course.Course', on_delete=models.CASCADE, null = True)
	
	def save(self, *args, **kwargs):
		if not self.id:
		# Newly created object, so set slug.
			self.lecture_title_slug = slugify(self.lecture_title)
			self.lecture_key_slug = slugify(self.lecture_key)
		super(Lecture, self).save(*args, **kwargs)

	def __str__(self):
		return self.lecture_title + ": " + str(self.pub_date)


class Attendant(models.Model):
	lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
	student_id = models.CharField(max_length=20)
	temp_id = models.CharField(max_length=20, default = "no code")
	position = models.CharField(max_length=20, default='N/A')
	connections = models.IntegerField(default=-1)
	pub_date = models.DateTimeField('date published', default = timezone.now())
	
	attendant_key_slug = models.SlugField(
		max_length=20, 
		null = True,
		unique = True, 
		editable = False)
		
	def save(self, *args, **kwargs):
		if not self.id:
		# Newly created object, so set slug.
			self.attendant_key_slug = slugify(self.temp_id)
		super(Attendant, self).save(*args, **kwargs)

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


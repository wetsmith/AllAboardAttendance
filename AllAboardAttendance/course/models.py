import datetime
#import lecture

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
#from lecture import models as Lecture
from accounts.models import Teacher

class Course(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	pub_date = models.DateTimeField('date published', default = timezone.now())
	course_title = models.CharField(max_length=50)
	course_title_slug = models.SlugField(
		max_length=50, 
		null = True,
		unique = True, 
		editable = False)

	# save overrides the default save function. It automatically makes our course_title_slug.
	# save also has broken link countermeasures.
	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug.
			self.course_title_slug = slugify(self.course_title)
			super(Course, self).save(*args, **kwargs)

	def __str__(self):
		return self.course_title + ": " + str(self.pub_date.year)


class Student(models.Model):
	student_id = models.CharField(max_length=20, default = 'student')
	student_id_slug = models.SlugField(max_length=20, default = 'student')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
	# save override here, just like in course. Automatically make our slugs from the student id.
	def save(self, *args, **kwargs):
		if not self.id:
			self.student_id_slug = slugify(self.student_id)
		super(Student, self).save(*args, **kwargs)

	def __str__(self):
		return self.student_id
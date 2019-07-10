from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.utils.text import slugify

import string,random

from lecture.views import create_lecture
from .models import Course, Student


class IndexView(generic.ListView):
	template_name = 'course/index.html'
	context_object_name = 'latest_course_list'

	def get_queryset(self):
		# ten most recent courses, in future we should make this more flexible
		return Course.objects.filter(
		    pub_date__lte=timezone.now()
		).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
	model = Course
	template_name = 'course/detail.html'

def get_queryset(self):
    """
    Excludes any courses that aren't published yet.
    """
    return Course.objects.filter(pub_date__lte=timezone.now())


def get_queryset(self):
	# returns the 10 most recent courses, can be expanded to all in future!
	return Course.objects.filter(
		pub_date__lte=timezone.now()
	).order_by('-pub_date')[:10]


# Converts a string into a slug for URL purposes.
# IMPORTANT for cleaner URLs, and in future, obfuscated URLs! 
#
# So, instead of
#	course/1/
# we can do
#	course/cs101-w19/
# or
#	course/1236sSSDvaskdaWE32S221s/
def return_slug(any_string):
	# get a slug of the string, generally a course_title. Uses django utility "slugify"
	return slugify(unicode('%s' % any_string))


#adds an instance of a lecture object to the course and fills it will all students in the course
#returns the instance of the lecture so it can be easily used (ie attendence list checking)
#Pre condition: course needs to be saved to the data base
def open_lecture(course, lecture_name = "lecture"):

	student_ids = course.student_set.values_list('student_id', flat = True)
	new_lecture = create_lecture(student_ids, lecture_name)
	course.lecture_set.add(new_lecture)
	return new_lecture

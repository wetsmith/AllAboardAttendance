from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.utils.text import slugify

import string,random

from lecture.views import create_lecture
from lecture.models import Lecture, Attendant, DirEdge
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
	slug_field = 'course_title_slug'
	slug_url_kwarg = 'course_title_slug'
	


class InfoView(generic.DetailView):
	model = Lecture
	template_name = 'course/info.html'
	slug_field = 'lecture_title_slug'
	slug_url_kwarg = 'lecture_title_slug'
	
class SignInView(generic.DetailView):
	model = Lecture
	template_name = 'course/signin.html'
	slug_field = 'lecture_key_slug'
	slug_url_kwarg = 'lecture_key_slug'


#adds an instance of a lecture object to the course and fills it will all students in the course
#returns the instance of the lecture so it can be easily used (ie attendence list checking)
#Pre condition: course needs to be saved to the data base
def open_lecture(request, course_id):

	course = get_object_or_404(Course, pk=course_id)
	lecture_title = request.POST.get('lecture_title')
	student_ids = course.student_set.values_list('student_id', flat = True)
	new_lecture = create_lecture(student_ids, lecture_title)
	course.lecture_set.add(new_lecture)
	
	next = request.POST.get('next', '/')
	return HttpResponseRedirect(next)
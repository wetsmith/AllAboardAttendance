from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.utils.text import slugify

import string,random

from lecture.views import create_lecture, sign_in, add_edge
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

	
	#captures form post and sends things via the request
	def post(self, request, *args, **kwargs):
		student__id = request.POST.get('student_id')
		lecture_pk = request.POST.get('lecture.pk')

		lecture = Lecture.objects.get(pk = lecture_pk)
		#checking if valid id entered  
		if(student__id in lecture.attendant_set.values_list('student_id', flat=True)):
			sign_in(lecture,student__id)
			student = lecture.attendant_set.get(student_id = student__id)
			return redirect('course:add_codes' , lecture.lecture_key_slug, student.attendant_key_slug)
			
			
		#I need to add some alert here to user but this redirects to form
		return render(request, self.template_name, {'lecture':lecture})
			
class AddCodeView(generic.DetailView):
	model = Attendant
	template_name = 'course/addcode.html'
	slug_field = 'attendant_key_slug'
	slug_url_kwarg = 'attendant_key_slug'
	
	'''context = self.get_context_data(**kwargs)
	attendant = context['attendant']
	lecture = attendant.lecture'''
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#getting the parent of attendant added for display on page
		context['lecture'] = context['object'].lecture
		return context
	
	def post(self, request, *args, **kwargs):
		student_code = request.POST.get('code')
		attendant_pk = request.POST.get('attendant.pk')
		attendant = Attendant.objects.get(pk=attendant_pk)
		lecture = attendant.lecture
		print(lecture.lecture_title)
		
		print(student_code,attendant_pk)
		
		#Check is user entered their own code
		if student_code == attendant.temp_id:
			user_message = "You do not count as your own peer"
		#check if code entered is valid
		elif(student_code in lecture.attendant_set.values_list('temp_id',flat=True)):
			# precondition: first_id is the drain (static id of student receiving id)
			#	second_id is the source (temporary id of student giving id)
			#   first <- second
			#	second -> first
			#returns message on whether they can add the student or not
			user_message = add_edge(lecture, attendant.student_id, student_code)
		else: #code does not exist in the data base
			user_message = "Peer Code entered does not exist"
		
		#this message needs to be sent to user
		print(user_message)
		
			
		#No matter what, redirects to same page. Students can add as many connections as they want. 
		return redirect('course:add_codes' , lecture.lecture_key_slug, attendant.attendant_key_slug)


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
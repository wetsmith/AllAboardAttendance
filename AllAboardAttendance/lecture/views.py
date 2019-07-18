from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import string, random

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import qrcode

from .models import Lecture, Attendant, DirEdge


class IndexView(generic.ListView):
	template_name = 'lecture/index.html'
	context_object_name = 'latest_lecture_list'

	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Lecture.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Lecture
	template_name = 'lecture/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Lecture.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Lecture
	template_name = 'Lecture/results.html'


def create_lecture(student_id_list = ['These','are', 'default', 'test', 'values'], name = 'default'):
	
	key = make_ran_url()
	checking = True
	while checking:
		all_lecs = Lecture.objects.values_list('lecture_key', flat = True)
		if key in all_lecs:
			key = make_ran_url()
		else:
			checking = False
		
	s = Lecture(lecture_title = name, lecture_key = key)
	s.save()

	make_lecture_qr(s)

	#student_id_list = ["Trevor", "Wesley", "Matt"] # temporary until parameter functionality done
	temp_id_list = make_id_list(len(student_id_list))
	for x in range(len(student_id_list)):
		s.attendant_set.create(student_id = student_id_list[x], temp_id = temp_id_list[x])

	return s


def create_attendance_lists(lecture, quota = 2):
	absent = lecture.attendant_set.filter(connections=-1).order_by('student_id')
	partial = lecture.attendant_set.filter(connections__range=(0,quota-1)).order_by('student_id')
	full = lecture.attendant_set.filter(connections__gte = quota).order_by('student_id')

	return [absent, partial, full]


def sign_in(lecture, identity):
	student = lecture.attendant_set.get(student_id = identity)
	if(student.connections == -1):
		student.one_up()
		student.save()


# precondition: first_id is the drain (static id of student receiving id)
#			   second_id is the source (temporary id of student giving id)
#			   first <- second
#			   second -> first
def add_edge(lecture, first_id, second_id):
	student_1 = lecture.attendant_set.get(student_id = first_id)
	student_2 = lecture.attendant_set.get(temp_id = second_id)

	if((len(student_1.diredge_set.filter(direction_id = student_2.student_id)) == 0) and (len(student_2.diredge_set.filter(direction_id = student_1.student_id)) == 0)): # check if edge added functionality to be implemented
		edge = student_2.diredge_set.create(direction_id = first_id)
		edge.save()
		student_1.one_up()
		student_1.save()
		student_2.one_up()
		student_2.save()
		return "connection success"
	else:
		return "connection failed: connection already exists"


def make_ran_url():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))


def make_id_list(class_size):
	temp_id = []

	for x in range(class_size):
		rand_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)) # hardcoded length of 5
		index = 0
		collisions = 0

		while(index < len(temp_id)):
			if (rand_id == temp_id[index]):
				rand_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))
				collisions += 1
				index = 0
			else:
				index += 1
		temp_id.append(rand_id)

	return temp_id



def identification(request, lecture_id): # will be replaced with a proper login page.
	lecture = get_object_or_404(Lecture, pk=lecture_id)
	try:
		entered_identity = lecture.attendant_set.get(student_id = request.POST['identity'])
	except (KeyError, Attendant.DoesNotExist):
		# Redisplay the attendant id entry form.
		return render(request, 'lecture/detail.html', {
			'lecture': lecture,
			'error_message': "You didn't enter a valid id.",
		})
	else:
		entered_identity.connections += 1
		entered_identity.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('lecture:results', args=(lecture.id,))) # in future, redirect to edge submission page.


# because QR codes are PIL images, they are saved twice. I haven't figured out a workaround.
def make_lecture_qr(lecture):
	# this is the URL I presumed holds the signin page for a lecture. Could be fixed down the line!
	url = "http://127.0.0.1:8000/course/" + lecture.lecture_key_slug + "/sign-in/"
	f = BytesIO()

	#generate qr code for it
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4,
	)
	qr.add_data(url)
	qr.make(fit=True)
	#saves generated QR code into images directory
	#can be modified like sending this image to somewhere else.
	img = qr.make_image()
	# this converts the PIL image into an image compatible with the ImageField in the DJango model.
	try:
		img.save(f, format='png')
		lecture.lecture_qr.save(lecture.lecture_title_slug, ContentFile(f.getvalue()))
	finally:
		f.close()

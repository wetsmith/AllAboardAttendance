from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.files.base import ContentFile


from PIL import Image
from io import BytesIO
from datetime import timedelta


import qrcode
import string, random
import os

import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm

import numpy as np


from .models import Lecture, Attendant, DirEdge

# This clas is a roundabout way of making sure that the dictionary keys match the database
# during the process when attendance information is taken. Only difference from normal 
# str() is that this one uses double quotes ("") as opposed to single quotes ('')
# Does it make sense? No, python strings are valid with both single and double quotes.
# Does it make the code work? Yes.
class str2(str):
	def __repr__(self):
		return ''.join(('"', super().__repr__()[1:-1], '"'))


def create_lecture(student_id_list = ['These','are', 'default', 'test', 'values'], name = 'default'):
	# make our random URL similar to how we make our student IDs.
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
	s.pub_date = timezone.now()
	s.save()
	make_lecture_qr(s)

	#student_id_list = ["Trevor", "Wesley", "Matt"] # temporary until parameter functionality done
	temp_id_list = make_id_list(len(student_id_list))
	for x in range(len(student_id_list)):
		s.attendant_set.create(student_id = student_id_list[x], temp_id = temp_id_list[x])

	return s


def create_attendance_lists(lecture, quota = 2):
	# quota for full attendance hardcoded for now. Future release will expand user functionality here.
	absent = lecture.attendant_set.filter(connections=-1).order_by('student_id')
	partial = lecture.attendant_set.filter(connections__range=(0,quota-1)).order_by('student_id')
	full = lecture.attendant_set.filter(connections__gte = quota).order_by('student_id')

	return [absent, partial, full]


def sign_in(lecture, identity):
	# timedelta represents lecture attendance window. hardcode for now - should be editable from user in future release
	if (timezone.now() <= lecture.pub_date + timedelta(minutes=15)):
		student = lecture.attendant_set.get(student_id = identity)
		if(student.connections == -1):
			student.one_up()
			student.save()
		return ""
	else:
		return "The lecture sign-in window has elapsed."


def add_edge(lecture, first_id, second_id):
	student_1 = lecture.attendant_set.get(student_id = first_id)
	student_2 = lecture.attendant_set.get(temp_id = second_id)


	# precondition: first_id is the drain (static id of student receiving id)
	#			   second_id is the source (temporary id of student giving id)
	#			   first <- second
	#			   second -> first

	if((len(student_1.diredge_set.filter(direction_id = student_2.student_id)) == 0) and (len(student_2.diredge_set.filter(direction_id = student_1.student_id)) == 0)): # check if edge added functionality to be implemented
		edge = student_2.diredge_set.create(direction_id = first_id)
		edge.save()
		student_1.one_up()
		student_1.save()
		student_2.one_up()
		student_2.save()
		generate_graph(lecture) # causes massive slowdown

		return "Connection Success"
	else:
		return "Connection Failed: connection already exists"


def make_ran_url():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))


def make_id_list(class_size):
	temp_id = []

	# the for loop generates a random ID made of uppercase ASCII characters and ASCII digits.
	# it then compares them against all other assigned random IDs in the lecture (O(n!)). Not
	# greatly efficient, but for lectures with <10,000 members it executes quickly enough.
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

# Creating a list of tuples with edge starting point and destination in order to create 
# the NetworkX graph in the generate_graph function.
def generate_graph(lecture):

	edge_list = []
	edge_time_list = []
	for attendant in lecture.attendant_set.all():
		for classmate in attendant.diredge_set.all():
			edge_list.append((str2(classmate.attendant.student_id), str2(classmate.direction_id)))
			edge_time_list.append(classmate.pub_date)

	attendance = nx.DiGraph()
	weights = {}
	g = BytesIO()

	# Add every single node and edge to the NetworkX graph, in addition to 
	# marking students as "present" by initializing weight to 0
	for (origin, destination) in edge_list:
		attendance.add_edge(origin, destination)
		weights[origin] = 0
		weights[destination] = 0

	node_names = []

	# Add proper number of connections associated with each student, both inbound and outbound
	# Create list for labelling nodes in graph
	for (origin, destination) in edge_list:
		weights[origin] = weights[origin] + 1 # not NetworkX weights. These are for printing.
		weights[destination] = weights[destination] + 1
		if origin not in node_names:
			node_names.append(origin)
		if destination not in node_names:
			node_names.append(destination)

	sizes = []
	names = {}
	# Create the actual node labels
	for n in node_names:
		names[str(n)] = n[:5] # first five characters of ID, add this to print connection count: + ": " + str(weights[n])
		sizes.append(70*len(n))
	
	light_blue = cmap_map(lambda x: x/2 + 0.5, matplotlib.cm.winter) # winter is a nice, theme-consistent color

	# Draw the NetworkX graph
	nx.draw_shell(attendance,
		node_size = 100,
		font_size = 2, 
		node_color=range(len(node_names)), # gradient colors 
		edge_color=range(len(edge_list)),
		cmap=light_blue, # node color is a mix of light greens through blues
		labels = names, 
		with_labels = True)
	try:
		# Save the image in a pseudofile in memory
		plt.savefig(g, format='png', dpi=500)
		# Save the image in the media directory so Django can find it
		lecture.lecture_graph.save(lecture.lecture_title_slug, ContentFile(g.getvalue()))
		# Clean up objects
		attendance.clear()
		plt.clf()
	finally:
		g.close()


	# https://scipy-cookbook.readthedocs.io/items/Matplotlib_ColormapTransformations.html
def cmap_map(function, cmap):
	""" Applies function (which should operate on vectors of shape 3: [r, g, b]), on colormap cmap.
	This routine will break any discontinuous points in a colormap.
	"""
	cdict = cmap._segmentdata
	step_dict = {}
	# Firt get the list of points where the segments start or end
	for key in ('red', 'green', 'blue'):
		step_dict[key] = list(map(lambda x: x[0], cdict[key]))

	step_list = sum(step_dict.values(), [])
	step_list = np.array(list(set(step_list)))
	# Then compute the LUT, and apply the function to the LUT
	reduced_cmap = lambda step : np.array(cmap(step)[0:3])
	old_LUT = np.array(list(map(reduced_cmap, step_list)))
	new_LUT = np.array(list(map(function, old_LUT)))
	# Now try to make a minimal segment definition of the new LUT
	cdict = {}
	for i, key in enumerate(['red','green','blue']):
		this_cdict = {}
		for j, step in enumerate(step_list):
			if step in step_dict[key]:
				this_cdict[step] = new_LUT[j, i]
			elif new_LUT[j,i] != old_LUT[j, i]:
				this_cdict[step] = new_LUT[j, i]
		colorvector = list(map(lambda x: x + (x[1], ), this_cdict.items()))
		colorvector.sort()
		cdict[key] = colorvector

	return matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)
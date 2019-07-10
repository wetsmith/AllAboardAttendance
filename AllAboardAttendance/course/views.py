from django.shortcuts import render
from lecture.views import create_lecture

# Create your views here.

#adds an instance of a lecture object to the course and fills it will all students in the course
#returns the instance of the lecture so it can be easily used (ie attendence list checking)
#Pre condition: course needs to be saved to the data base
def open_lecture(course, lecture_name = "lecture"):
	
	student_ids = course.student_set.values_list('student_id', flat = True)
	l = create_lecture(student_ids,lecture_name)
	course.lecture_set.add(l)
	return l
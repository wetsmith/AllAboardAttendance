import random, string

# Parses student models for the number of connections made, and sorts them
# into three lists:
#	not present (unconnected)
#	partially present (not met connection quota)
#	fully present (met or exceeded connection quota)

# In the future, the connection quota may be passed as a parameter.

def compile_attendance_list():

	# begin test value generation
	n = 100 # number of students
	m = 10  # maximum number of connections for a student
	quota = 5
	static_id = ["".join(random.choices(string.ascii_lowercase, k = 5)) for _ in range(n)]
	connections = [random.randrange(m) for _ in range(n)]
	student_connections = dict(zip(static_id, connections))
	# end test value generation

	not_present = []
	part_present = []
	full_present = []

	# filling in presence lists
	for student in student_connections:
		if student_connections[student] == 0:
			not_present.append(student)
		elif student_connections[student] < quota:
			part_present.append(student)
		else:
			full_present.append(student)

	# compiling list of lists
	attendance_list = [not_present, part_present, full_present]

	return attendance_list
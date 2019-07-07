import random, string

######################################################
# Takes a list of static student ids (CruzIDs, for instance) and creates
# a unique temporary ID for each static ID, returned as a dictionary
# where each static id is paired to temporary id.
#####################################################
# TIME COMPLEXITY:
#	runtime for 1000 students: 0.1 second.
#	runtime for 10000 students: 15 seconds.
#	runtime for 100000 students: FORGET ABOUT IT.
#
# This is because of the naive collision checker. When the nth random id
# is generated, it must be compared to n-1 ids.
# I think that's O(n!) runtime. Not good.
#
# HOWEVER, expected input size is obviously < 1000.
# 1000 students has a runtime of ~0.1 second so I'm not going to dedicate
# time to making an efficient collision checker just yet.


def make_id_dictionary():

	# IN FUTURE: static_id will be passed as input, not generated in-function. 
	# Also, we might consider using UUID in the future for temp-ids. Right now it's just
	# a randomly assembled string, checked for collision against the rest.
	
	# Begin random id list for testing. NOT COLLISION CHECKED!
	n = 10000
	static_id = ["".join(random.choices(string.ascii_lowercase, k = 5)) for _ in range(n)]
	# End random id list for testing.

	temp_id = []

	for x in static_id:
		
		# Currently, temporary id length is hardcoded (k=5), and consists only of uppercase letters and digits
		# We might want to make these user-adjustable parameters down the line.
		rand_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

		# Begin collision checker and counter.
		# This is also where the runtime blowup comes from!
		index = 0
		collisions = 0
		while index < len(temp_id):
			if rand_id == temp_id[index]:
				rand_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
				index = 0
				collisions += 1 # track number of collisions for debug purposes
			else:
				index += 1
		temp_id.append(rand_id)
		# End collision checker and counter.

	id_dictionary = dict(zip(static_id, temp_id))

	return id_dictionary
	# collisions are highly improbable for expected input size, but ARE CHECKED FOR ANYWAYS.
	# Future versions may just check for collisions after full batch, and fix the collided values then.
	# For now, though, it's fine I'd wager.

	# example id_dictionary:
	# {'billy': 'PIW28', 'bobby': 'II1EH', 'janet': 'B0JIK', 'julia': 'AN4FI', 'peter': 'OD8F4', 'polly': '0549J', 'phil': 'NBG6C'}
	
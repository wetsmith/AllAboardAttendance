from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Session, Attendant, DirEdge


class IndexView(generic.ListView):
    template_name = 'session/index.html'
    context_object_name = 'latest_session_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Session.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Session
    template_name = 'session/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Session.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Session
    template_name = 'session/results.html'


def create_session(student_id_list = None):
    s = Session()
    s.save()

    student_id_list = ["Trevor", "Wesley", "Matt"] # temporary until parameter functionality done
    temp_id_list = make_id_list(len(student_id_list))

    for x in range(len(student_id_list)):
        s.attendant_set.create(student_id = student_id_list[x], temp_id = temp_id_list[x])
    
    return s


def create_attendance_lists(session, quota = 2):
    absent = session.attendant_set.filter(connections=-1).order_by('student_id')
    partial = session.attendant_set.filter(connections__range=(0,quota-1)).order_by('student_id')
    full = session.attendant_set.filter(connections__gte = quota).order_by('student_id')

    return [absent, partial, full]


def sign_in(session, identity):
    student = session.attendant_set.get(student_id = identity)
    if(student.connections == -1):
        student.one_up()
        student.save()

# precondition: first_id is the drain (static id of student receiving id)
#               second_id is the source (temporary id of student giving id)
#               first <- second
#               second -> first
def add_edge(session, first_id, second_id):
    student_1 = session.attendant_set.get(student_id = first_id)
    student_2 = session.attendant_set.get(temp_id = second_id)

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

def identification(request, session_id): # will be replaced with a proper login page.
    session = get_object_or_404(Session, pk=session_id)
    try:
        entered_identity = session.attendant_set.get(student_id = request.POST['identity'])
    except (KeyError, Attendant.DoesNotExist):
        # Redisplay the attendant id entry form.
        return render(request, 'session/detail.html', {
            'session': session,
            'error_message': "You didn't enter a valid id.",
        })
    else:
        entered_identity.connections += 1
        entered_identity.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('session:results', args=(session.id,))) # in future, redirect to edge submission page.


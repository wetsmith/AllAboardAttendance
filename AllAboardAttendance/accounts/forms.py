
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Teacher
#extends the basic user form in order for it to point at user
class CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Teacher
        fields = ('username', 'email')

class ChangeForm(UserChangeForm):

    class Meta:
        model = Teacher
        fields = ('username', 'email')
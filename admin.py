from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CreationForm, ChangeForm
from .models import Teacher

#updates our changes for admin to use
class CustAdmin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = Teacher
    list_display = ['email', 'username',]

admin.site.register(Teacher)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from .models import Teacher

@admin.register(Teacher)
class UserAdmin(DjangoUserAdmin):
	#editable teacher fields
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name')}),
	)
	#required feilds for teacher creation
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)
	#teacher orginization in admin
	list_display = ('email', 'first_name', 'last_name', 'is_staff')
	#ways to search for a Teacher
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('is_staff','email')#user ordering
admin.site.unregister(Group)#groups are not being used in any way so they are removed
from django.contrib import admin
from .models import Lecture, Attendant, DirEdge

admin.site.register(Lecture)
admin.site.register(Attendant)
admin.site.register(DirEdge)
# Register your models here.

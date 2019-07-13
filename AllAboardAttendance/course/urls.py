from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:course_title_slug>/', views.DetailView.as_view(), name='detail'),
	path('<slug:course_title_slug>/<int:pk>/', views.open_lecture, name='open_lecture')
	#path(r'^connect/(?P<course>.+)/(?P<pk>\d+)/$', views.open_lecture, name='open_lecture')
]

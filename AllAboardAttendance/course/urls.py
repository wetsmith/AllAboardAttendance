from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:course_title_slug>/', views.DetailView.as_view(), name='detail'),
	#Something is broken here I think? Getting NoReverseMatch , but can't find another reason on here:
	#https://www.pythoncircle.com/post/424/solving-django-error-noreversematch-at-url-with-arguments-and-keyword-arguments-not-found/
	path('<slug:course_title_slug>/<int:pk>/', views.open_lecture, name='open_lecture')
	#path(r'^connect/(?P<course>.+)/(?P<pk>\d+)/$', views.open_lecture, name='open_lecture')
]

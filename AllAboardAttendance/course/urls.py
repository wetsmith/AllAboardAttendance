from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:course_title_slug>/', views.DetailView.as_view(), name='detail'),
	path('<int:course_id>/open-lecture/', views.open_lecture, name='open_lecture'),
	path('<slug:lecture_title_slug>/', views.LectureInfoView, name='lectureinfo'),
]

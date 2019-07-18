from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:course_title_slug>/', views.DetailView.as_view(), name='detail'),
	path('<int:course_id>/open-lecture/', views.open_lecture, name='open_lecture'),
	path('<slug:lecture_title_slug>/info/', views.InfoView.as_view(), name='info'),
	path('<slug:lecture_key_slug>/sign-in/', views.SignInView.as_view(), name='sign_in'),
	path('<slug:lecture_key_slug>/add-codes/', views.sign_inTTT, name='add_codes'),
]

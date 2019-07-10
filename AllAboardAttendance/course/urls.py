from django.urls import path

from . import views

app_name = 'course'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:course_title>/', views.DetailView.as_view(), name='detail'),
]

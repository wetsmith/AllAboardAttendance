from django.urls import path

from . import views

app_name = 'lecture'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('course/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('course/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('course/<int:lecture_id>/identification/', views.identification, name='identification'),
]

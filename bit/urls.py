from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.login, name='login'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('patientdash/', views.patientdash, name='patientdash'),
    path('doctordash/', views.doctordash, name='doctordash'),
    path('disease/', views.disease, name='disease'),
    path('map/', views.default_map, name="default"),
    path('chart/', views.home, name='chart'),
    path('chart1/', views.home1, name='chart1'),
    path('chart2/', views.home2, name='chart2'),
    path('chart3/', views.home3, name='chart3'),
]

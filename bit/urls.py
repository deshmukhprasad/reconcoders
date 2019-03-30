from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from .import views


urlpatterns = [
    path('', views.login, name='login'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
    path('patientdash/', views.patientdash, name='patientdash'),
    path('doctordash/', views.doctordash, name='doctordash'),
    path('disease/', views.disease, name='disease'),
    path('map/', views.default_map, name="default"),
    path('chart1/', views.home1, name='home'),
    path('chart2/', views.home2, name='home'),
    path('chart3/', views.home3, name='home'),
    path('blood/', views.blood, name = 'blood'), 
    path('success', views.success, name = 'success'), 
    path('hotel_images', views.display_hotel_images, name = 'hotel_images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
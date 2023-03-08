from django.urls import path
from django.urls import include
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('',
         mainapp.accommodations,
         name='index'),
    path('auth/',
         include('authapp.urls', namespace='auth')),
    path('accommodation_details/<int:pk>/',
         mainapp.accommodation,
         name='accommodation'),
]

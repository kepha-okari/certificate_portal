from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.new_application, name='applyCertificate'),
    path('reports/', views.reports, name='reports'),
]
from django.urls import path

from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('doctorlogin', LoginView.as_view(template_name='doctor/doctorlogin.html'),name='doctorlogin'),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
]

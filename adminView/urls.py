from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='adminlogin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('bloodbank_index/', views.bloodbank_index, name='bloodbank_index'),
    path('donation/requests/', views.admin_view_donation_requests, name='admin_view_donation_requests'),
    path('receiver-request/list/', views.admin_receiver_request_list, name='admin_receiver_request_list'),

]

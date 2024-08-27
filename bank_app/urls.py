from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.LogOut, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('loginview/', views.loginview, name='loginview'),
    path('register/', views.register, name='register'),
    path('reset_profile/', views.reset_profile, name='reset_profile'),
    path('linking_page/', views.linking_view, name='linking_view'),
    path('otp/', views.otp, name='otp'),
    path('imf/', views.imf, name='imf'),
    path('aml/', views.aml, name='aml'),
    path('tac/', views.tac, name='tac'),
    path('vat/', views.vat, name='vat'),
    path('pending/', views.pending, name='pending'),
    path('profile/', views.profile, name='profile'),
    path('loans/', views.loans, name='loans'),
    path('analytics/', views.analytics, name='analytics'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('kyc/', views.kyc, name='kyc'),
    path('bank_transfer/', views.bank_transfer, name='bank_transfer'),
]
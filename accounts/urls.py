from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/', views.signupaccounts, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
]
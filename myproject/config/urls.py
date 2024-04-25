from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    # path('token_send' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('token_send/', views.token_send, name='token_send'), 
    path('config/login/' , login_attempt , name="login_attempt"),

]






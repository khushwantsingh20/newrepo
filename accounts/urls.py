from django.urls import path, include
#resetpws
from django.urls import path
from accounts.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ProfileView,edit_profile
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from django.urls import path
# from .views import EditProfileView

from .views import *
urlpatterns = [
    
    path('logout/', logout_user, name='logout'),
    #reset
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    #resetconfirm
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
           #confirm
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='signin.html'),
         name='password_reset_complete'),
#     
    path("signin",signin, name='signin'),
    path('change-password/', change_password, name='change_password'),
    path('activate/<str:uidb64>/<str:token>/',activate, name='activate'),
    path('signup', signup, name='signup'),
    
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/',edit_profile, name='edit_profile'),
   
    
]









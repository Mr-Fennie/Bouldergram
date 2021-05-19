from django.urls import path
from .views import (UserSignUpView, UserUpdateView, PasswordsChangeView,
                    UserProfilePageView, EditProfilePageView, CreateProfileView )
#from django.contrib.auth import views as auth_views
from . import views

#from . import views


urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('profile/edit/', UserUpdateView.as_view(), name='profile_edit'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html') ),
    path('profile/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html') ),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', UserProfilePageView.as_view(), name='user_profile_page' ),
    path('<int:pk>/profile/edit/page', EditProfilePageView.as_view(), name='edit_profile_page' ),
    path('profile/create/', CreateProfileView.as_view(), name='create_profile_page' ),



]

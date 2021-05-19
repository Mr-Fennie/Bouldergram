from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileEditForm, PasswordEditForm, ProfilePageForm, UpdateProfilePageForm
from blog.models import UserProfile




# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = UserProfile.objects.all()
        context = super(UserProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    form_class = UpdateProfilePageForm
    template_name = 'registration/update_user_profile.html'

    success_url = reverse_lazy('home')



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordEditForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserSignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    form_class = ProfileEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

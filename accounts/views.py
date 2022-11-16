from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from accounts.forms import ProfileForm, SignupUserForm
from accounts.models import CustomUser


# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        return render(request, 'accounts/profile.html', {
            'user_data' : user_data,
        })

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial = {
                'first_name' : user_data.first_name,
                'last_name' : user_data.last_name,
                'user_name' : user_data.user_name,
                'department' : user_data.department,
            }
        )

        return render(request, 'accounts/profile_edit.html',{
            'form' : form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.first_name = form.cleaned_data['first_name']
            user_data.last_name = form.cleaned_data['last_name']
            user_data.user_name = form.cleaned_data['user_name']
            user_data.department = form.cleaned_data['department']
            user_data.save()
            return redirect('profile')


        return render(request, 'accounts/profile.html', {
            'form' : form
        })

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm

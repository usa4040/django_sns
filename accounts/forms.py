from allauth.account.forms import SignupForm
from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    user_name = forms.CharField(max_length=30, label='ユーザーネーム')
    department = forms.CharField(max_length=30, label='所属', required=False)
    picture = forms.ImageField(label='プロフィール画像', required=False)

class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    user_name = forms.CharField(max_length=30, label='ユーザーネーム')
    department = forms.CharField(max_length=10, label='所属', required=False)
    picture = forms.ImageField(label='プロフィール画像', required=False)

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_name = self.cleaned_data['user_name']
        user.department = self.cleaned_data['department']
        user.picture = self.cleaned_data['picture']
        user.save()
        return user

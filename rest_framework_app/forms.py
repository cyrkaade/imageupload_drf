from django.forms import ModelForm
from .models import myUser
from django.contrib.auth.forms import UserCreationForm

# User forms that gain information about them

class UserForm(ModelForm):
    class Meta:
        model = myUser
        fields = "__all__"

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = myUser
        fields = ['name', 'username', 'email', 'password1', 'password2']
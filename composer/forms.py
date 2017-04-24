from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import  authenticate,login
from .models import Project,Song

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email','username','password']

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if username and password:
            user = User.objects.get(username=username)
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active!")
        return super(LoginForm,self).clean(*args,**kwargs)

class ProjectForm(forms.ModelForm):

    class Meta:

        model = Project
        fields = ['name']

class SongForm(forms.ModelForm):

    class Meta:

        model = Song
        fields = ['file']
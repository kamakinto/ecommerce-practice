from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(
    widget=forms.PasswordInput
  )

class RegisterForm(forms.Form):
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(
    widget=forms.PasswordInput
  )
  password2 = forms.CharField(
  widget=forms.PasswordInput,
  label="Confirm Password"
)
  def clean_username(self):
    data = self.cleaned_data
    username = self.cleaned_data.get("username")
    qs = User.objects.filter(username=username)
    if qs.exists():
      raise forms.ValidationError("Username is taken")
    return data

  def clean_email(self):
    data = self.cleaned_data
    email = self.cleaned_data.get("email")
    qs = User.objects.filter(email=email)
    if qs.exists():
      raise forms.ValidationError("Email is taken")
    return data

  def clean(self):
    print("Inside clean function")
    data = self.cleaned_data
    password = data.get("password")
    password2 = data.get("password2")
    if password2 != password:
      print("passwords dont match")
      raise forms.ValidationError("Passwords must match")
    return data
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm
from .forms import LoginForm, RegisterForm


def home_page(request):
  context = {
    "title": "Hello from the homepage",
     "premium_content": "Yeeaaaahhhh premium content!",
  }
  if request.user.is_authenticated:
    print("user is authenticated")

  return render(request, "home_page.html", context)

def about_page(request):
  context = {
    "title": "hello from the about page"
   }
  return render(request, "about_page.html", context)

def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context = {
    "title": "hello from the contact page mfers",
    "content": "content for the contact page",
    "form": contact_form
    }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)

  # if request.method == "POST":
  #     print(request.POST.get('fullname'))
  #     print(request.POST.get('email'))
  #     print(request.POST.get('content'))
  return render(request, "contact/view.html", context)

def  login_page(request):
  form = LoginForm(request.POST or None)
  context = {
    "form": form
  }
  print(request.user.is_authenticated)
  if form.is_valid():
   print(form.cleaned_data)
   username = form.cleaned_data.get("username")
   password = form.cleaned_data.get("password")
   user = authenticate(request, username=username, password=password)
   print(request.user.is_authenticated)
   if user is not None:
     print(request.user.is_authenticated)
     login(request, user)
     context['form'] = LoginForm() #adds an empty login form after user is logged in.
     return redirect("/")
  else:
    print("Error") #return an invalid login error message
  return render(request, "auth/login.html", context)
User = get_user_model()
def  register_page(request):
  register_form = RegisterForm(request.POST or None)
  context = {
    "register_form": register_form
  }
  if register_form.is_valid():
    print(register_form.cleaned_data)
    username = register_form.cleaned_data.get("username")
    email = register_form.cleaned_data.get("email")
    password = register_form.cleaned_data.get("password")
    new_user = User.objects.create_user(username, email, password)
    print(new_user)
  return render(request, "auth/register.html", context)

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



from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm

def  login_page(request):
        form = LoginForm(request.POST or None)
        context = {
        "form": form
        }
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        if form.is_valid(): #if the form is clean, begin the log-in authentication process
                print(form.cleaned_data)
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)

                if user is not None: #if we have found a user, log them in, and handle the redirect
                        login(request, user)
                        context['form'] = LoginForm() #adds an empty login form after user is logged in.
                        if is_safe_url(redirect_path, request.get_host()):
                                return redirect(redirect_path)
                        else:
                                return redirect('/')
                else:
                        print("Error") #return an invalid login error message
        return render(request, "accounts/login.html", context)


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
        return render(request, "accounts/register.html", context)

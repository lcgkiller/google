
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):

    return render(request, "member/login.html")


def signup(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(reverse("Sign Up OK"))

    else:
        userform = UserCreationForm()

    return render(request, 'member/signup.html', {'userform': userform})


def signup_ok(request):
    return render(request, 'member/signup_ok.html')

# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from member.forms import MyUserCreationForm

User = get_user_model()


def login(request):

    return render(request, "member/login.html")

# user = super(UserForm, self).save(commit=False)
#  user.set_password(self.cleaned_data["password"])
#  if commit:
#      user.save()
#  return user

def signup(request):

    if request.method == "POST":
        userform = MyUserCreationForm(request.POST)
        if userform.is_valid():
            print(request.POST)
            userform = User.objects.create_user(username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'])
            userform.save()
            return redirect("member:signup_ok")

    else:
        userform = MyUserCreationForm()

    return render(request, 'member/signup.html', {'userform': userform})


def signup_ok(request):
    return render(request, 'member/signup_ok.html')
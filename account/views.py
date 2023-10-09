from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm, EditForm


def login_page(request):
    context = {'errors':[]}

    if request.user.is_authenticated:
        return redirect("home:home_page")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get("username"))
            login(request , user)
            return redirect("home:home_page")
    else:
        form = LoginForm()
    return render(request , "account/login.html" , {'form': form})


def log_out(request):
    logout(request)
    return redirect("home:home_page")


def register_page(request):
    if request.user.is_authenticated:
        return redirect("home:home_page")

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            confirm_password = form.cleaned_data.get('confirm_password')
            user = User.objects.create(username=username , email=email , password=confirm_password)
            login(request , user)
            return redirect("home:home_page")
    else:
        form = SignUpForm()

    return render(request , "account/register.html" , {'form': form})

def edit_page(request):

    if not request.user.is_authenticated:
        return redirect("home:home_page")

    user = request.user
    form = EditForm(instance=user)
    if request.method == "POST":
        form = EditForm(instance=user , data=request.POST)
        if form.is_valid():
            form.save()

    return render(request , 'account/EditForm.html' , {'form': form , 'user' : user})

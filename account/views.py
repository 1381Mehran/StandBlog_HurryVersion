from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User

def login_page(request):
    context = {'errors':[]}

    if request.user.is_authenticated:
        return redirect("home:home_page")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request , username=username , password=password)

        if user is not None :
            login(request , user)
            return redirect("home:home_page")
        else:
            context['errors'].append("User is not Exist")
            return render(request , "account/login.html" , context)

    return render(request , "account/login.html")


def log_out(request):
    logout(request)
    return redirect("home:home_page")


def register_page(request):

    context = {'errors': []}

    if request.user.is_authenticated:
        return redirect("home:home_page")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            context['errors'].append("Passwords are not same")
            return render(request, "account/register.html" , context)

        user = User.objects.create(username=username , email=email , password=password2)
        login(request , user)
        return redirect("home:home_page")

    return render(request , "account/register.html")


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import profile


@login_required(login_url="signin")
def index(request):
    pro = profile.objects.get(user=request.user)
    return render(request, "index.html", {"user_profile": pro})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already in use")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "username exists")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()

                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)

                profile_new = profile.objects.create(user=user, id_user=user.id)
                profile_new.save()
                return redirect("settings")

        else:
            messages.error(request, "Password not matching")

    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        usrname = request.POST["username"]
        passwd = request.POST["password"]

        user = auth.authenticate(username=usrname, password=passwd)  # Fixed typo here
        print(user, usrname, passwd)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("signin")
    else:
        ...

    return render(request, "signin.html")


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect("signin")


@login_required(login_url="signin")
def settings(request):
    user_profile = profile.objects.get(user=request.user)

    if request.method == "POST":
        if request.FILES.get("image") is None:
            image = user_profile.profileimg
        else:
            image = request.FILES.get("image")
        bio = request.POST["bio"]
        location = request.POST["location"]

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()

        return redirect("/")
    return render(request, "settings.html", {"user_profile": user_profile})


def upload(request):
    return HttpResponse("<h1>upload view</h1>")

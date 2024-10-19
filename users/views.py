from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse   
from django.contrib.auth import login, logout, authenticate
# Create your views here.

# Index page will display the authenticated users' info
def index(request):
    # if the user is not authenticated, it will be redirected to login view
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "users/user.html")
 
# 1. first login view present a form that users can login themselves   
# 2. the login view will authenticate the user and if successful, user will be directed to
# 3. the index view to see the users' info.
# 4. if not exist it will show the user does not exist.
# 
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username =username, password =password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message": "User logged out"
    })
    
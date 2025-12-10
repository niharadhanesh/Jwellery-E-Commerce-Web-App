from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def landing(request):
    return render(request,'landing.html')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # If user is superadmin → redirect to admin dashboard
            if user.is_superuser:
                return redirect("admin_dashboard")  # Named URL of your admin dashboard

            # If normal user → redirect to home page
            return redirect("home")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")   # Your custom login page


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def logout_view(request):
    logout(request)
    return redirect('landing') 
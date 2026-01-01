from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
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

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validation
        if not all([full_name, email, username, password, confirm_password]):
            messages.error(request, "All fields are required.")
            return redirect("register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        # Split full name
        name_parts = full_name.split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")

        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect("register")

    return render(request, "register.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def logout_view(request):
    logout(request)
    return redirect('landing') 
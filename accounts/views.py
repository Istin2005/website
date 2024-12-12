from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save user
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to homepage or dashboard
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def user_details(request):
    users = User.objects.all()
    return render(request, 'user_details.html', {'users': users})

def user_list(request):
    # Get all usernames from the User model
    users = User.objects.all()

    # Pass the data to the template
    return render(request, 'user_list.html', {'users': users})
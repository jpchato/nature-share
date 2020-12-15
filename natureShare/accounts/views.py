from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
# Create your views here.

User = get_user_model()

def user_register(request):
    if request.method == 'POST':
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        return redirect('login')
    return render(request, 'accounts/register.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request, 
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None: 
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    # return HttpResponse('youve been logged out')
    return render(request, 'natureShareApp/home.html')
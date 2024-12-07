from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# def homepage(request):
#     return render(request,'homepage.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('items:index')
        else:
            # messages.success(request,("User not found, Please check your credentials"))
            return redirect('login')
    else:
        return render(request,'registration/login.html',{})

def logout_user(request):
    logout(request)
    # messages.success(request,("You are logged out"))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Registration Succcessful"))
            return redirect('items:index')
    else:
        form = UserCreationForm()     

    return render(request,'registration/register_user.html',{'form':form})

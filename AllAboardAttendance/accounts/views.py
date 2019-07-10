from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth

'''
I added signup, login, logout functionality. 
It basically uses Django's built in tools about authentication. 

If you look at accounts/templages folder, then there's some html files about below view's. 
'''

def signup(request):
    if request.method == "POST":
        if request.POST["password1"]==request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'username or password incorrect'})
    return render(request, 'login.html')

#For logout, I don't know about the mehtod post, so I just let it log out whenever we call that request.
#it didn't worked when below lines were added.
def logout(request):
    #if request.method == "POST":
    auth.logout(request)
    return redirect('home')
    #return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def iregister(request):
    if request.method == 'POST':
        username   = request.POST['name']
        email      = request.POST['email']
        pass1      = request.POST['pass']
        pass2      = request.POST['re_pass']

        #Validate password
        if pass1 != pass2:
            messages.error(request, "Password don't match. Ty again")
            return render(request, 'todo_app/register.html')
        
        #check for existing email
        if myUser.objects.filter( email=email ).exists():
            messages.error( request, "A similar email already exists. Choose another one." )
            return render( request, 'todo_app/register.html' )
        
        user = myUser.objects.create( username = username ,email=email)
        user.set_password(pass1)
        user.is_active= True
        user.save()
        return redirect( 'login' )
    return render(request, 'todo_app/register.html')

def ilogin(request):
    if request.method == 'POST':
        email = request.POST ['email']
        password = request.POST['your_pass']
        try:
            get_object_or_404(myUser, email= email )
            user = authenticate( request , username=email ,password=password )
            if user is not None:
                login(request, user)
                messages.success( request, f' welcome {email}')
                return redirect( 'index' )
            else:
                messages.error(request, 'Invalid login credentials')
        except Http404:
            messages.error(request, f'Account with {email} does not exist. Create account to continue')
        return render( request,'todo_app/login.html', {'email':email} )
    else:
        return render(request, 'todo_app/login.html')
    
def ilogout(request):
    logout(request)
    return redirect( 'login' )

@login_required()
def index(request):
    context= {}
    users = myUser.objects.all()
    context['users'] = users
    return render(request, 'todo_app/index.html', context)
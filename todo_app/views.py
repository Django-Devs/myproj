from django.shortcuts import render

# Create your views here.
def iregister(request):
    return render(request, 'todo_app/register.html')

def ilogin(request):
    return render(request, 'todo_app/login.html')
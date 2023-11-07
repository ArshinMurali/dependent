from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('logins')
        else:
            messages.info(request,'invalid password')
            return redirect('register')

    return render(request,'register.html')

def logins(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['password']
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, 'Try again')
            return redirect('logins')
    return render(request,'logins.html')

def new(request):

    return render(request,'new.html')

# def form(request):
#
#     return render(request, 'dependantfield.html')
#
#
# def last(request):
#     return render(request,'submit.html')

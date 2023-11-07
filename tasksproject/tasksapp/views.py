from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.
def Main(request):
    return render(request,'main.html')
def Login(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['password']
        user = auth.authenticate(username=a, password=b)
        if user is None:
            messages.info(request, 'You need to register')
            return redirect('login')
        else:
            messages.info(request, 'You need to register')
            return redirect('login')
    return render(request,'login.html')

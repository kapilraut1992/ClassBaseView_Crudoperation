from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def registerView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')

    template='Accountapp/register.html'
    context={'form':form}
    return render(request,template,context)



def loginView(request):
    if request.method=="POST":
        uname=request.POST.get('usename')
        pas=request.POST.get('passw')
        user=authenticate(username=uname,password=pas)
        if user is not None:
            login(request,user)
            return redirect('addlaptop')
    template='Accountapp/login.html'
    context={}
    return render(request,template,context)


def logoutView(request):
    logout(request)
    return redirect('loginPage')


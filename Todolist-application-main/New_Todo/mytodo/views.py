
from django.shortcuts import render,redirect
from .models import todo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mytodo.forms import RegistrationForm




# Create your views here.

def registerpage(request):
    if request.method == "POST":
 
        form = RegistrationForm(request.POST)
 
        if form.is_valid():
            form.save()
             
            
            messages.success(request,f'a new user has been registered')
            return redirect('mytodo:login')


    else:
        form = RegistrationForm

        
    return render(request,'mytodo/registration.html',{'form':form})



def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

    #    this is used to authenticate user
        if user is not None:
            login(request,user)
            return redirect('mytodo:index')

    return render(request,'mytodo/login.html')


def logoutpage(request):
    logout(request)
    return redirect('mytodo:login')


@login_required(login_url='mytodo:login')
def index(request):
    mytodo = todo.objects.all()
    
    if request.method == 'POST':
        if request.POST['title'].strip() == "":
            return redirect('mytodo:index')
        title = request.POST['title']
        new_todo = todo(title=title)
        new_todo.save()
        return redirect('mytodo:index')
    
    return render(request,'mytodo/index.html',{'mytodo':mytodo})



# the delete view makes use of GET methos because we are using 
# a dynamic url link to get 
# and delete object using thier id or pk

def delete_view(request,id):
    mytodo = todo.objects.get(id=id)
    if request.method == 'GET':
        mytodo.delete()
        return redirect('mytodo:index')
    

    
    
    
    
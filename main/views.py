from django.shortcuts import render, redirect
from .models import *

# Render Templates
def index(request):
    return render(request, 'index.html')

def load_dashboard(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'dashboard.html', context)

def view_list(request, id):
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'view_list.html', context)

# login reg functions
def process_login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        user = user[0]
        if user.password == request.POST['password']:
            request.session['user_id'] = user.id
            return redirect('/dashboard')
    return redirect('/')

def process_register(request):
    # if confirmation is same as password, then create new user
    if request.POST['password'] == request.POST['password_conf']:
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user_id'] = new_user.id
        return redirect('/dashboard')
    else:
        return redirect('/')

# list functions
def create_list(request):
    current_user = User.objects.get(id=request.session['user_id'])
    new_list = TaskList.objects.create(name=request.POST['name'], icon=request.POST['icon'], created_by=current_user)
    redirect('/dashboard')

def add_listItem(request):
    redirect('/dashboard')
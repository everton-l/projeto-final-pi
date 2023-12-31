from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            print(login_form.data)
            if user is not None:
                login(request, user)
                if user.get_username() == "admin":
                    return redirect('admin')
                
                else:
                    return redirect('listagem')

    else:
        login_form = LoginForm()

    context = {'form': login_form}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user.save()
            return redirect('login')

    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'users/create.html', context)
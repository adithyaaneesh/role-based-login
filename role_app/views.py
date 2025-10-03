from django.shortcuts import redirect, render
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == 'POST':
        form_data = UserRegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login')
    else:
        form_data = UserRegistrationForm()
    return render(request,'register.html',{'form':form_data}) 

        
def user_login(request):
    if request.method == 'POST':
        user_data = LoginForm(request, data=request.POST) 
        if user_data.is_valid():
            user = user_data.get_user() 
            login(request, user)
            if user.profile.role == 'admin':
                return redirect('dashboard')
            elif user.profile.role == 'user':
                return redirect('userdashboard')
            else:
                return redirect('staffdashboard')
    else:
        user_data = LoginForm()
    return render(request, 'login.html', {'form':user_data})



def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')
@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard')


def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:     
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'form' : form})



class UserLoginView(LoginView):
    template_name = 'app/login.html'

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')
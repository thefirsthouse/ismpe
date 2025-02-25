from django.contrib.auth import login, aauthenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomUserCreationForm


# class RegisterView(View):
#     def get(self, request):
#         form = CustomUserCreationForm()
#         return render(request, 'accounts/register.html', {'form': form})
    

#     def post(self, request):
#         form = CustomUserCreationForm()
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#         return render(request, 'accounts/register.html', {'form': form})


# class LoginView(View):
#     def get(self, request):
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/')
#         return render(request, 'accounts/login.html', {'form': form})

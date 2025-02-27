from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm


def users_list(request)


# def add_user(request):
#     if request.method == "GET":
#         form = CustomUserCreationForm(request.GET)
#         return render(request, "administration/edit_user.html", {"form": form})
#     elif request.method == "POST":
#         if form.is_valid():
#             return HttpResponseRedirect("/")
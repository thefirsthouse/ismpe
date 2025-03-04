from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from accounts.models import CustomUser
from accounts.urls import urlpatterns as accounts_urls
from courses.models import Course, Assignment, Submission


def index(request):
    if request.user.is_authenticated == False:
        return redirect(accounts_urls[0])
    
    return render(request, "logic/index.html")

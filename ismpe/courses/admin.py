from django.contrib import admin

from .models import Course, Assignment, Submission

models = (Course, Assignment, Submission)

for model in models:
    admin.site.register(model)

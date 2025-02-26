from django.db import models
from accounts.models import CustomUser

class Course(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="course_authors")
    name = models.CharField("Course title", max_length=255, unique=True)
    description = models.TextField("Description", blank=True)
    students = models.ManyToManyField(CustomUser, related_name="enrolled_courses")

    def __str__(self):
        return self.name


class Assignment(models.Model):
    TYPES_OF_ASSIGNMENT = [
        ("lecture", "Lecture"),
        ("manual", "Manual"),
        ("file", "File"),
        ("essay", "Essay"),
        ("test", "Test"),
        ("exam", "Exam"),
    ]

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="assignment_authors")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_assignments")
    type = models.CharField("Type of assignment", max_length=8, choices=TYPES_OF_ASSIGNMENT)
    title = models.CharField("Title", max_length=255, unique=True)
    description = models.TextField("Description", blank=True)
    deadline = models.DateTimeField("Deadline")

    def __str__(self):
        return self.title


class Submission(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="submission_authors")
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="assignment_submissions")
    file = models.FileField("File", upload_to="courses/student_files", blank=True, null=True)
    answer_text = models.TextField("Answer text", blank=True, null=True)
    answer_test = models.JSONField("Test answers", blank=True, null=True)

    send_at = models.DateTimeField("Send at", auto_now_add=True)
    grade = models.IntegerField("Grade", blank=True, null=True)

    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name} - {self.assignment.title}"
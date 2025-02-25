from django.db import models

from accounts.models import CustomUser

TYPES_OF_ASSIGNMENT = [
    ('lecture', 'Lecture'),
    ('manual', 'Manual'),
    ('file', 'File'),
    ('essay', 'Essay'),
    ('test', 'Test'),
    ('exam', 'Exam')
]

class Course(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="course_authors")
    name = models.CharField(name="Course title", max_length=255, unique=True)
    description = models.TextField(name="Description", blank=True)
    students = models.ManyToManyField(CustomUser, related_name='related_courses')

    def __str__(self):
        return self.name


class Asignment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="asignment_authors")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_asignments")
    type = models.CharField(name="Type of asignment", max_length=8, choices=TYPES_OF_ASSIGNMENT)
    title = models.CharField(name="Title", max_length=255, unique=True)
    description = models.TextField(name="Description", blank=True)
    deadline = models.DateTimeField(name="Deadline")

    def __str__(self):
        return self.title


class Submission(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='submission_authors')
    assignment = models.ForeignKey(Asignment, on_delete=models.CASCADE, related_name="assignment_submissions")
    file = models.FileField(name="File", upload_to='courses/student_files', default=None)
    answer_text = models.TextField(name="Answer text", blank=True, null=True)
    answer_test = models.JSONField(name="Test answers", blank=True, null=True)

    send_at = models.DateTimeField(name="Send at", auto_now_add=True)
    grade = models.IntegerField(name="Grade", blank=True)

    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name} - {self.assignment.title}"

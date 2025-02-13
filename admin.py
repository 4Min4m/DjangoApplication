from django.contrib import admin
from .models import Course, Question, Choice, Submission  # Import your models

admin.site.register(Course)  # Existing registration
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)

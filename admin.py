from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):  # Or admin.StackedInline for a different layout
    model = Choice
    extra = 3  # Number of empty choice fields to display

class QuestionInline(admin.TabularInline):  # Or admin.StackedInline
    model = Question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline] # Include choices when editing questions

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin) # Register with QuestionAdmin
admin.site.register(Choice) # You can register Choice separately if needed
admin.site.register(Submission)

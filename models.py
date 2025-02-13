from django.db import models
from django.utils import timezone

class Question(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='questions')  # Link to Course
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')  # Link to Question
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)  # Mark correct answer

    def __str__(self):
        return self.choice_text
from django.contrib.auth.models import User  # Import User model
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s submission for {self.course.name}"

from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=200)
    create_date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("quiz:detail", kwargs={'pk': self.pk})


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=CASCADE, default=1)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

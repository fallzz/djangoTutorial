import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):       #Subclass of django.db.models.Model class
    question_text=models.CharField(max_length=200)
    pub_date=models.DateField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return (timezone.localtime() - datetime.timedelta(days=1)) <= self.pub_date <= timezone.localtime()

class Choice(models.Model):         #Subclass of django.db.models.Model class
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
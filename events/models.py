from datetime import date
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published.')

    def was_published_recently(self):
        return self.pub_date >= timezone.localtime() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return '{} published at {}'.format(self.question_text, self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return '{} relations to {}'.format(self.choice_text, self.question)
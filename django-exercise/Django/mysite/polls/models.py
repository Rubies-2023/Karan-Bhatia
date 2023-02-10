from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Registration(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    photo = models.ImageField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name', 'photo']



    def __str__(self):
        return self.first_name

class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice,on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    voter = models.ForeignKey(User, on_delete=models.CASCADE,related_name='votes')
    #choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

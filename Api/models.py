from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Poll(models.Model):
    question = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.question
 
class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.answer_text
    

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """ Category model for questions"""
    name    = models.CharField(blank=False, max_length=50)
    

    def __str__(self):
        return self.name




class Question(models.Model):
    """ Model for the questions in encyclopedia"""

    user     = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ManyToManyField(to=Category)
    question = models.CharField(blank=False, max_length=250)
    


    def __str__(self):
        return self.question





class Answer(models.Model):
    """ Model for answers of Questions """
    user      = models.ForeignKey(to=User, on_delete=models.CASCADE)
    questions = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    text      = models.CharField(blank=False, max_length=50)
    value     = models.BooleanField(default=True)

    def __str__(self):
        return self.text
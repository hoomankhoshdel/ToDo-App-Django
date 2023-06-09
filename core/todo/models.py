from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

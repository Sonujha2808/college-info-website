from django.db import models

# Create your models here.
class faculty(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()

from django.db import models

# Create your models here.

class todo(models.Model):
    title = models.CharField(max_length=20)
    

    def __str__(self):
        return self.title

class signup_form(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)


from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name
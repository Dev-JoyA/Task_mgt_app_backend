from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.username

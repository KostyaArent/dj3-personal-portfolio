from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Fact(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return str(self.pk)


class ProgLanguage(models.Model):
    title = models.CharField(max_length= 30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Developer(models.Model):
    call_sign = models.CharField(max_length=10)
    languages = models.ManyToManyField(ProgLanguage)
    facts = models.ManyToManyField(Fact)
    user = models.ForeignKey(User, unique=True, related_name='profile', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user)

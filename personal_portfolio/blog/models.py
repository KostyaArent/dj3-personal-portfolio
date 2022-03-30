from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=60)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField()
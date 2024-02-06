from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.TextField()
    image=models.ImageField(upload_to='media')
    url=models.TextField()

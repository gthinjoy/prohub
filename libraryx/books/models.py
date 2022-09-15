from django.db import models

# Create your models here.
class Book(models.Model):
    name= models.CharField(max_length= 250)
    author= models.CharField(max_length= 250)
    description = models.TextField()
    year = models.IntegerField()
    image= models.ImageField(upload_to='album')


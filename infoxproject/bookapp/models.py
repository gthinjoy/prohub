from django.db import models

# Create your models here.
class  Books(models.Model):
    name=models.CharField(max_length=250)
    author=models.CharField(max_length=150)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='album')

    def  __str__(self):
        return  self.name
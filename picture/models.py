from django.db import models

# Create your models here.
class Location (models.Model):
    location=models.CharField(max_length =100)

class Picture(models.Model):
    image=models.ImageField(upload_to='pictures/')
    title =models.CharField(max_length = 100)
    description= models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE,default='Nairobi')


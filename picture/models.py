from django.db import models

# Create your models here.
class Location (models.Model):
    location=models.CharField(max_length =100)

    def save_location(self):
        self.save()
    def delete_location(self):
        self.save_location()
        self.delete()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Picture(models.Model):
    title =models.CharField(max_length = 100)
    description= models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


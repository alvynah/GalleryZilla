from django.shortcuts import render,HttpResponse
from .models import Picture,Location,Category

# Create your views here.
def welcome(request):
    pictures = Picture.objects.all()
    return render(request,'all-pictures/index.html',{'pictures':pictures})


from operator import mod
from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(null=True,blank=True,max_length=200)
    keywords = models.CharField(null=True,blank=True,max_length=300)
    wordCount = models.CharField(null=True,blank=True,max_length=100)

    def __str__(self):
        return self.title

class BlogSection(models.Model):
    title = models.CharField(null=True,blank=True,max_length=200)
    body = models.TextField(null=True,blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    keywords = models.CharField(null=True,blank=True,max_length=300)
    wordCount = models.CharField(null=True,blank=True,max_length=100)

    def __str__(self):
        return self.title

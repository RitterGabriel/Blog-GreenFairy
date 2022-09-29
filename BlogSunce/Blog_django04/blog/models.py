
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    image = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


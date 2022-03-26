from django.db import models

# Create your models here.



class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

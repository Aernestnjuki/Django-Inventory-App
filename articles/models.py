from django.db import models

# Create your models here.

class Articles(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # default=django.utils.timezone.now
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models
from django.utils import timezone

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
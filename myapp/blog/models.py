from django.db import models
from django.utils import timezone

# Create your models here.

class Blogs(models.Model):
    BLOG_TYPE = [
        ('P', 'Personal'),
        ('W', 'Work'),
        ('H', 'Health'),
        ('S', 'School'),
        ('O', 'Others'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=BLOG_TYPE, default='')
    
    def __str__(self):
        return self.title
    
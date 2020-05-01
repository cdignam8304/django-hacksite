from django.db import models
from datetime import datetime

# Create your models here.

class Hack(models.Model):
    
    hack_title = models.CharField(max_length=200)
    hack_content = models.TextField()
    hack_published = models.DateTimeField("date published", default=datetime.now())
    # hack_series = # placeholder for foreign key
    hack_slug = models.CharField(max_length=200, default=1)
    
    def __str__(self):
        return self.hack_title
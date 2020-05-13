from django.db import models
from datetime import datetime
import os
from django.conf import settings

# Create your models here.
    

class HackCategory(models.Model):
    
    hack_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)
    category_photo = models.ImageField(
                                        upload_to="media",
                                        default = os.path.join(settings.MEDIA_URL,"lifehacks.jpg")
                                        )
    
    class Meta():
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.hack_category


class HackSeries(models.Model):
    
    hack_series = models.CharField(max_length=200)
    hack_category = models.ForeignKey(HackCategory,
                                      default=1,
                                      verbose_name="Category",
                                      on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    series_photo = models.ImageField(upload_to="media",
                                       default = os.path.join(settings.MEDIA_URL,"lifehacks.jpg"))
    
    class Meta():
        verbose_name_plural = "Series"
    
    def __str__(self):
        return self.hack_series


class Hack(models.Model):
    
    hack_title = models.CharField(max_length=200)
    hack_content = models.TextField()
    hack_published = models.DateTimeField("date published", default=datetime.now())
    hack_series = models.ForeignKey(HackSeries,
                                    default=1,
                                    verbose_name="Series",
                                    on_delete=models.SET_DEFAULT)
    hack_slug = models.CharField(max_length=200, default=1)
    
    def __str__(self):
        return self.hack_title
    
    def get_absolute_url(self):
        return f"/{self.hack_slug}/"
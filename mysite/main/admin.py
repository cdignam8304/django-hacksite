from django.contrib import admin
from .models import Hack, HackSeries, HackCategory
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class HackAdmin(admin.ModelAdmin):
    
    fieldsets = [
            ("Title/date", {"fields":["hack_title", "hack_series", "hack_slug", "hack_published"]}),
            ("Content", {"fields":["hack_content"]}),
        ]
    # fieldsets = [
    #         ("Title/date", {"fields":["hack_title", "hack_slug", "hack_published"]}),
    #         ("Content", {"fields":["hack_content"]}),
    #     ]
    
    formfield_overrides = {
            models.TextField: {"widget": TinyMCE()}
        }

admin.site.register(HackSeries)
admin.site.register(HackCategory)
admin.site.register(Hack, HackAdmin)
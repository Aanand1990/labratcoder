from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    pub_date = models.DateTimeField(blank=True)
    body = HTMLField()


from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    pub_date = models.DateTimeField(blank=True)
    body = models.TextField(blank=True)


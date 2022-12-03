from django.db import models

class Tracker(models.Model):
    date = models.DateTimeField()
    weight = models.FloatField(null=True)
    waist = models.FloatField(null=True)
    stomach = models.FloatField(null=True)
    chest = models.FloatField(null=True)
    butt = models.FloatField(null=True)
    thighs = models.FloatField(null= True)
    calves = models.FloatField(null=True)
    code_written = models.FloatField(null=True)
    article_url = models.URLField(null=True)

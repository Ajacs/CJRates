from django.db import models

# Create your models here.

class ExhangeRate(models.Model):
    rate = models.CharField(max_length=150)
    last_update = models.DateTimeField()
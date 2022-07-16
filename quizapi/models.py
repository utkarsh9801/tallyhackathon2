from django.db import models

from django.db import models

# Create your models here.
class scoreModel(models.Model):
    username = models.CharField(max_length = 500)
    score = models.IntegerField()
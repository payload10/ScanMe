from turtle import mode
from django.db import models

class File(models.Model):
    document = models.FileField(upload_to='files/',blank=True)
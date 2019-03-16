from django.db import models
from datetime import datetime


# Create your models here.
class AccidentAlert(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    time = models.DateTimeField(default=datetime.now, blank=True)
    camera_num = models.CharField(max_length=50)

from django.db import models

# Create your models here.

class movies_detail(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

class event_detail(models.Model):
    event_image = models.ImageField(upload_to='images/')
    event_summary = models.CharField(max_length=200)

    def __str__(self):
        return self.event_summary




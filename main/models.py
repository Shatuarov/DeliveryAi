# main/models.py

from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

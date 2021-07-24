from django.db import models

class Footar(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Link = models.URLField(max_length=400, blank=True)
    Icon = models.ImageField(upload_to='Social_icon/', blank=False)
    Website_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.Name

# Create your models here.

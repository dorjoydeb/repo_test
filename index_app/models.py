from django.db import models

#Home page

class Index_Top_bar(models.Model):
    Name = models.CharField(max_length=20, blank=True)
    Background_Image = models.ImageField(upload_to='Home_page_top_bar/', blank=False)
    Title = models.CharField(max_length=50, blank=False)
    Sub_title = models.CharField(max_length=100, blank=False)
    Link = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.Name


# Create your models here.

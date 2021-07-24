from django.db import models

#About page

class About_top_bar(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Background_image = models.ImageField(upload_to='Home_page_top_bar/', blank=False)
    Title = models.CharField(max_length=50, blank=False)
    Sub_title = models.CharField(max_length=100, blank=False)
    Link = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.Name

class About_main_content(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Main_content = models.TextField(max_length=500, blank=False)
    Image = models.ImageField(upload_to='About_body_section_image', blank=True)

    def __str__(self):
        return self.Name

# Create your models here.

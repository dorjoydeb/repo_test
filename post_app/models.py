from django.db import models

#Post page

class Post_top_bar(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Background_image = models.ImageField(upload_to='Home_page_top_bar/', blank=False)
    Title = models.CharField(max_length=50, blank=False)
    Sub_title = models.CharField(max_length=100, blank=False)
    Link = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.Name

class Post_Blog_sections(models.Model):
    Blog_Name = models.CharField(max_length=50, blank=False)
    Blog_title = models.CharField(max_length=100, blank=False)
    Sub_title = models.CharField(max_length=200, blank=True)
    Description = models.CharField(max_length=1000, blank=False)
    Image = models.ImageField(upload_to='Blog_images/', blank=True)

    def __str__(self):
        return self.Blog_name
# Create your models here.

from django.db import models

class Contact_top_bar(models.Model):
    Name = models.CharField(max_length=20, blank=True)
    Background_image = models.ImageField(upload_to='Home_page_top_bar/', blank=False)
    Title = models.CharField(max_length=50, blank=False)
    Sub_title = models.CharField(max_length=100, blank=False)
    Link = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.Name

class Contact_body_section(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Description = models.TextField(max_length=400, blank=False)

    def __str__(self):
        return self.Name

class Contact_email_section(models.Model):
    Name = models.CharField(max_length=20, blank=False)
    Email = models.EmailField(max_length=20, blank=False)
    Subject = models.CharField(max_length=100, blank=False)
    Description = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return ('Name :'+ self.Name + ' & ' + 'Email :'+ self.Email)


# Create your models here.

# Generated by Django 3.2.5 on 2021-07-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Top_bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20)),
                ('Background_Image', models.ImageField(upload_to='Home_page_top_bar/')),
                ('Title', models.CharField(max_length=50)),
                ('Sub_title', models.CharField(max_length=100)),
                ('Link', models.URLField(blank=True, max_length=400)),
            ],
        ),
    ]
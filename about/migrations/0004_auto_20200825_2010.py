# Generated by Django 3.0.8 on 2020-08-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_pagecontent_content_loc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='content_loc',
            field=models.CharField(choices=[('AboutContent', 'About'), ('HomeCarousel', 'Carousel'), ('HomeMarketing', 'Marketing'), ('ProductContent', 'Products')], default='HomeMarketing', max_length=100),
        ),
    ]

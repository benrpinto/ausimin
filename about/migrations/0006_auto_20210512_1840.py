# Generated by Django 3.0.8 on 2021-05-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20210511_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='content_loc',
            field=models.CharField(choices=[('AboutContent', 'About'), ('HomeCarousel', 'Carousel'), ('HomeMarketing', 'Marketing'), ('ProductContent', 'Products'), ('CertContent', 'Certification'), ('ApplContent', 'Applications')], default='HomeMarketing', max_length=100),
        ),
    ]

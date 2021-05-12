# Generated by Django 3.0.8 on 2021-05-12 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210511_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(blank=True, max_length=100)),
                ('aka_text', models.CharField(blank=True, max_length=2000)),
                ('purity_text', models.CharField(blank=True, max_length=2000)),
                ('standards_text', models.CharField(blank=True, max_length=2000)),
                ('sizes_text', models.CharField(blank=True, max_length=2000)),
                ('specs_text', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='content_loc',
            field=models.CharField(choices=[('AboutContent', 'About'), ('HomeCarousel', 'Carousel'), ('HomeMarketing', 'Marketing'), ('ProductContent', 'Products'), ('CertContent', 'Certification'), ('ApplContent', 'Applications')], default='HomeMarketing', max_length=100),
        ),
        migrations.CreateModel(
            name='UsesContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_text', models.CharField(blank=True, max_length=2000)),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductContent')),
            ],
        ),
    ]
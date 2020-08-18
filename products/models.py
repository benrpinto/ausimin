from django.db import models

# Create your models here.

class FeatureContent(models.Model):
   title_text = models.CharField(blank=True, max_length=100)
   subtitle_text = models.CharField(blank=True, max_length=100)
   main_text = models.CharField(blank=True, max_length=1000)
   content_loc = models.CharField(max_length=100)

   def __str__(self):
      return self.content_loc + '(' + self.title_text + ')'

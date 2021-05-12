from django.db import models

# Create your models here.

class SiteContent(models.Model):
   title_text = models.CharField(blank=True, max_length=100)
   main_text = models.CharField(blank=True, max_length=2000)
   class Meta:
      abstract = True

   def __str__(self):
      return self.title_text + ' (' + str(self.id) + ')'

class FeatureContent(SiteContent):
   subtitle_text = models.CharField(blank=True, max_length=100)
   class Meta:
      abstract = True

class CarouselContent(SiteContent):
   pass

class HomeContent(FeatureContent):
   pass

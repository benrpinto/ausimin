from django.db import models

# Create your models here.

class SiteContent(models.Model):
   LOCATION_CHOICES = (
      ('AboutContent', 'About'),
      ('HomeCarousel', 'Carousel'),
      ('HomeMarketing', 'Marketing'),
      ('ProductContent', 'Products'),
   )
   title_text = models.CharField(blank=True, max_length=100)
   main_text = models.CharField(blank=True, max_length=2000)
   content_loc = models.CharField(default = "HomeMarketing", max_length=100, choices=LOCATION_CHOICES)
   class Meta:
      abstract = True

   def __str__(self):
      return self.content_loc + '(' + self.title_text + ')'

class FeatureContent(SiteContent):
   subtitle_text = models.CharField(blank=True, max_length=100)
   class Meta:
      abstract = True

class CarouselContent(SiteContent):
   pass

class PageContent(SiteContent):
   pass

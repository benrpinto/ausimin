from django.contrib import admin
from .models import PageContent
from .models import CarouselContent
# Register your models here.
admin.site.register(CarouselContent)
admin.site.register(PageContent)

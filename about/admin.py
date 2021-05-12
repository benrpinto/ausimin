from django.contrib import admin
from .models import AboutContent
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
   readonly_fields = ('id',)

admin.site.register(AboutContent,ContentAdmin)

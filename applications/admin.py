from django.contrib import admin
from .models import ApplContent
# Register your models here.
class ContentAdmin(admin.ModelAdmin):
   readonly_fields = ('id',)

admin.site.register(ApplContent,ContentAdmin)

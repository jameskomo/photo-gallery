from django.contrib import admin
from .models import Image, Location, tags, Category

class LocationAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Image)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category)
admin.site.register(tags)

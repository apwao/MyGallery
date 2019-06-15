from django.contrib import admin
from .models import Image,Location,Category,tags

# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(tags)



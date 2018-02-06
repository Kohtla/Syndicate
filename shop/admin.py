from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Colour)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Bucket)
admin.site.register(Detail)


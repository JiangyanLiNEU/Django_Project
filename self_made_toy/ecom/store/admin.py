from django.contrib import admin

# Register your models here.
from .models import Item

admin.site.register(Item)

admin.site.header = 'Store Admin'
admin.site.site_title = "Ecom Admin Area"
admin.site_index_title = 'Welcome to Ecom Admin Page'

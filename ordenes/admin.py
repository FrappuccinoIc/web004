from django.contrib import admin
from .models import Client, Category, Ot

#class CategoryAdmin(admin.ModelAdmin)

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Ot)
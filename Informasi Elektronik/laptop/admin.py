from django.contrib import admin

from .models import Laptop

class showKet(admin.ModelAdmin):
    readonly_fields = ['slug','publish']

admin.site.register(Laptop,showKet)

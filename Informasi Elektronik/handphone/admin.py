from django.contrib import admin
from . models import Handphone

class PhoneAdmin(admin.ModelAdmin):
    readonly_fields =['slug','publish','update']

admin.site.register(Handphone,PhoneAdmin)

# Register your models here.

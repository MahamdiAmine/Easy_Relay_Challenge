from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.Client)
admin.site.register(models.Order)

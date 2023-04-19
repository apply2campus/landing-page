from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.leads)
admin.site.register(models.newsletters)
admin.site.register(models.contact)

from django.contrib import admin
from .models import data_point



class data_pointAdmin(admin.ModelAdmin):
   readonly_fields = ('created',)

admin.site.register(data_point, data_pointAdmin)



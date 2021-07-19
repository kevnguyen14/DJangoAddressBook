from django.contrib import admin
from . models import Contact
# Register your models here.
# register a class model to use admin crud operations on within the admin webpage
admin.site.register(Contact)


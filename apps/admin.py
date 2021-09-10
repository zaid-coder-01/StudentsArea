from django.contrib import admin

# Register your models here.
from apps.models import Facts, Document

admin.site.register(Facts)
admin.site.register(Document)
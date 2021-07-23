from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Author
# Register your models here.

admin.site.register(Author, PageAdmin)
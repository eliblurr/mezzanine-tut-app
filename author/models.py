from django.db import models
from mezzanine.pages.models import Page

# Create your models here.

class Author(Page):
	dob = models.DateField("Date of birth")

class Book(models.Model):
    author = models.ForeignKey("Author")
    title = models.CharField(max_length=200, default='')
    cover = models.ImageField(upload_to="authors")
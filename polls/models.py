from django.db import models
from mezzanine.pages.models import Page

# Create your models here.

class Poll(Page):
	pub_date = models.DateTimeField("Date published")

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
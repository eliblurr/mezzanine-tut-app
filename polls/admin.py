from django.contrib import admin

from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin  import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Poll, Choice

# Register your models here.



poll_extra_fieldsets = ((None, {"fields": ("pub_date",)}),)

class ChoiceInline(TabularDynamicInlineAdmin):
	model = Choice 
    
class PollAdmin(PageAdmin):
	inlines = (ChoiceInline,)
	fieldsets = (deepcopy(PageAdmin.fieldsets) + poll_extra_fieldsets)
	
admin.site.register(Poll, PollAdmin)
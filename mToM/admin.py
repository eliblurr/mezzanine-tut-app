from django.contrib import admin
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import NRSAPage,Event,NRSANewsEvent,NRSANewsEventCategory
from copy import deepcopy

# Register your models here.

from mezzanine.core.admin import (
    BaseTranslationModelAdmin,
    DisplayableAdmin,
    OwnableAdmin,
)

class NRSANewsEventCategoryAdmin(BaseTranslationModelAdmin):
    fieldsets = ((None, {"fields": ("title",)}),)



nrsa_news_event_admin_fieldsets = deepcopy(PageAdmin.fieldsets)
nrsa_news_event_admin_fieldsets[0][1]["fields"].insert(1, "categories")
nrsa_news_event_admin_fieldsets = list(nrsa_news_event_admin_fieldsets)

nrsa_news_event_extra_fieldsets = ((None, {"fields": ("featured",
    "featured_image","feature_pictured")}),)


class NRSANewsEventAdmin(PageAdmin):

    fieldsets = nrsa_news_event_admin_fieldsets  + list(nrsa_news_event_extra_fieldsets)
    filter_horizontal = (
        "categories",
        "related_news",
    )

admin.site.register(NRSAPage,PageAdmin)

admin.site.register(NRSANewsEvent,NRSANewsEventAdmin)
admin.site.register(NRSANewsEventCategory,NRSANewsEventCategoryAdmin)

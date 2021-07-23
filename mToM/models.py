from django.db import models
from  mezzanine.pages.models import Page, RichText
from mezzanine.core.models import  Slugged
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.utils.models import AdminThumbMixin, upload_to

# Create your models here.

class RichTextMixin(RichText):
    edit_as_html = models.BooleanField(default=False)

    class Meta:
        abstract = True

class NRSANewsEventCategory(Slugged):
    """
    A category for grouping news posts into a series.
    """
    class Meta:
        verbose_name = _("News Category")
        verbose_name_plural = _("News Categories")
        ordering = ("title",)

    @models.permalink
    def get_absolute_url(self):
        return reverse("nrsa_news_events_list_category", kwargs={"nrsa_news_event_category": self.slug})



class NRSAPage(Page,RichTextMixin):
    cover_pix = models.ImageField(upload_to="nrsa_pages")


class NRSANewsEvent(Page,RichTextMixin,AdminThumbMixin):

    categories = models.ManyToManyField(
        "NRSANewsEventCategory",
        verbose_name=_("Categories"),
        blank=True,
        related_name="news_events",
    )

    feature_pictured = models.ImageField(upload_to="news_event",null=True,blank=True)
    featured = models.BooleanField(default=False)
    featured_image = FileField(
        verbose_name=_("Featured Image"),
        upload_to=upload_to("nrsa.NRSANewsEvent.featured_image", "news_event"),
        format="Image",
        max_length=255,
        null=True,
        blank=True,
    )

    related_news = models.ManyToManyField(
        "self", verbose_name=_("Related news"), blank=True
    )

    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("News event")
        verbose_name_plural = _("News events")
        ordering = ("-publish_date",)

class Event(Page):
    cover_pix = models.ImageField(upload_to="nrsa_pages")

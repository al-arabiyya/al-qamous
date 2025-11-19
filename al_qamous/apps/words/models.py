"""Home page"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from al_qamous.cms.blocks import MediaBlock


# Create your models here.
class WordIndex(Page):
    """Word index page"""

    content = StreamField(
        MediaBlock(),
        null=True,
        blank=True,
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "word"
    template = "al_qamous/word.html"
    content_panels = Page.content_panels + [FieldPanel("content")]
    parent_page_types = ["home.Home"]
    subpage_types = ["al_qamous_words.WordIndex"]


class AbstractWord(Page):
    """Abstract base class for words"""

    description = RichTextField(
        verbose_name=_("description"),
        help_text=_("Page description"),
    )
    content = StreamField(
        MediaBlock(),
        null=True,
        blank=True,
        verbose_name=_("content"),
        help_text=_("Page content"),
    )
    related = models.ManyToManyField(
        "self",
        symmetrical=True,
        verbose_name=_("related"),
        help_text=_("Related words"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("related"),
    ]

    class Meta:
        """Meta data"""

        abstract = True


class WordRoot(AbstractWord):
    """Root of a Word"""

    length = models.PositiveSmallIntegerField(
        default=3,
        verbose_name=_("length"),
        help_text=_("Root length"),
    )

    context_object_name = "word"
    template = "al_qamous/root.html"
    content_panels = AbstractWord.content_panels + [FieldPanel("length")]
    parent_page_types = ["al_qamous_words.WordIndex"]
    subpage_types = ["al_qamous_words.Word"]


class Word(AbstractWord):
    """Word page"""

    context_object_name = "word"
    template = "al_qamous/word.html"
    parent_page_types = ["al_qamous_words.WordRoot"]
    subpage_types = []

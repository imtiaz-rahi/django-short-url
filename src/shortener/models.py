from django.conf import settings
from django.urls import reverse
from django.db import models
from django_hosts.resolvers import reverse
from .validators import validate_url, validate_dot_com
from .utils import create_shortcode

# Safer way: will not break code if we forget to define it
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
SHORTCODE_MIN = settings.SHORTCODE_MIN


# Create your models here.
class KirrUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(KirrUrlManager, self).all(*args, **kwargs).filter(active=True)

    def refresh_shortcodes(self, items=None):
        """Change (update) shortcodes of all URL records in the database"""
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        count = 0
        for ob in qs:
            ob.shortcode = create_shortcode(ob)
            ob.save()
            count += 1
        return f'Refreshed shortcode count: {count}'


# noinspection SpellCheckingInspection
class KirrURL(models.Model):
    """Model definition for KirrURL."""

    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = KirrUrlManager()

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self, 15)
        super(KirrURL, self).save(*args, **kwargs)

    class Meta:
        # ordering = '-url' # Change ordering of all queries by default
        verbose_name = 'KirrURL'
        verbose_name_plural = 'KirrURL'

    def __str__(self):
        """Unicode representation of KirrURL."""
        return str(self.url)

    def get_short_url(self):
        return reverse('shorturl', kwargs={'shortcode': self.shortcode}, port='8000', scheme='http')
        # return reverse("shorturl", kwargs={'shortcode': self.shortcode})  # works
        # return "/a/{sc}".format(sc=self.shortcode)

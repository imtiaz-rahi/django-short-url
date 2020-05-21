import random
import string
from django.db import models


def code_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
# noinspection SpellCheckingInspection
class KirrURL(models.Model):
    """Model definition for KirrURL."""

    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'KirrURL'
        verbose_name_plural = 'KirrURL'

    def __str__(self):
        """Unicode representation of KirrURL."""
        return str(self.url)

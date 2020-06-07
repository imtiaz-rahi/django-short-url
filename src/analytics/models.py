from django.db import models
from shortener.models import KirrURL

class ClickEventManager(models.Manager):
    def add_event(self, instance):
        if isinstance(instance, KirrURL):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    """Model definition for ClickEvent."""
    kirr_url= models.OneToOneField(KirrURL)
    count   = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    class Meta:
        """Meta definition for ClickEvent."""
        verbose_name = 'ClickEvent'
        verbose_name_plural = 'ClickEvents'

    def __str__(self):
        return '{i}'.format(i=self.count)

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views import View

import inspect
from .models import KirrURL


# Create your views here.
def kerr_redirect_view(request, shortcode=None, *args, **kwargs):
    """Function based view"""
    # obj = KirrURL.objects.get(shortcode=shortcode)
    if settings.DEBUG:
        print(f'view : {shortcode}')
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count() == 1:
    #     obj_url = qs.first().url
    # return HttpResponse(f'Function {inspect.stack()[0][3]} Hello: {obj_url}')


def whoami():
    return inspect.getframeinfo(inspect.currentframe()).function


class KerrRedirectView(View):
    """Class based view"""

    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse(f"class {self.__class__.__name__} says Hello: {shortcode}")

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views import View

import inspect

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import KirrURL


# Create your views here.
class HomeView(View):

    def get(self, request, *args, **kwargs):
        if settings.DEBUG:
            print(request.GET)
        ctx = {
            'h1title': 'kirr.co shortener',
            'form': SubmitUrlForm()
        }
        return render(request, "shortener/home.html", context=ctx)

    def post(self, request, *args, **kwargs):
        frm = SubmitUrlForm(request.POST)
        template = "shortener/home.html"
        ctx = {
            'h1title': 'kirr.co shortener',
            'form': frm
        }
        if frm.is_valid():
            obj, created = KirrURL.objects.get_or_create(url=frm.cleaned_data.get("url"))
            template = "shortener/created.html" if created else "shortener/exists.html"
            ctx = {
                "object": obj,
                "created": created
            }
        return render(request, template, ctx)

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
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if not qs.exists() or qs.count() != 1:
            raise Http404
        # obj = get_object_or_404(KirrURL, shortcode=shortcode)
        obj = qs.first()
        ClickEvent.objects.add_event(obj)
        return HttpResponseRedirect(obj.url)
        # return HttpResponse(f"class {self.__class__.__name__} says Hello: {shortcode}")

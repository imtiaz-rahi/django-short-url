"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static

from shortener.views import HomeView, kerr_redirect_view, KerrRedirectView

# https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
    url(r'^djadmin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="Homepage"),
    url(r'^view-1/$', kerr_redirect_view),
    url(r'^view-2/$', KerrRedirectView.as_view()),
    # url(r'(?P<shortcode>[\w-]+){6,15}/$', kerr_redirect_view),    # wrong
    # url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
    url(r'a/(?P<shortcode>[\w-]{4,15})/$', KerrRedirectView.as_view(), name='shorturl'),
    url(r'b/(?P<shortcode>[\w-]+)/$', kerr_redirect_view),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL', 'http://www.kirr.co')


def wildcard_redirect(request, path=None, *args, **kwargs):
    return HttpResponseRedirect(f'{DEFAULT_REDIRECT_URL}/{path}' if path is not None else DEFAULT_REDIRECT_URL)

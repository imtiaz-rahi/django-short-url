import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 8)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, csize=SHORTCODE_MIN):
    new_code = code_generator(size=csize)
    is_exists = instance.__class__.objects.filter(shortcode=new_code).exists()
    return create_shortcode(csize=csize) if is_exists else new_code

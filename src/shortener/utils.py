import random as rn
import string as st
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

#from shortener.models import  KirrURL

def code_Generator(size = SHORTCODE_MIN, chars = st.ascii_lowercase + st.digits):
    return ''.join(rn.choice(chars) for _ in range(size))

def create_Shortcode(instance, size = 6):
    new_code = code_Generator(size = size)
    #print(instance)
    #print(instance.__class__)
    #print(instance.__class__.__name__)
    Klass = instance.__class__
    qsExists = Klass.objects.filter(shortcode = new_code).exists()
    if qsExists:
        return create_Shortcode(size = size)
    return new_code
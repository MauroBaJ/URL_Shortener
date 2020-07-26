from django.db import models
from .utils import create_Shortcode, code_Generator
from django.conf import settings
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class KirrURL_Manager(models.Manager):

    def all(self, *args, **kwargs):
        qsMain = super(KirrURL_Manager, self).all(*args, **kwargs)
        qs = qsMain.filter(active = True)
        return qs

    def refresh_shortcodes(self, items = None):
        #print(items)
        qs = KirrURL.objects.filter(id__gte = 1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_Shortcode(q)
            #print(q.shortcode)
            print(q.id)
            q.save()
            new_codes += 1    
        return "New codes made: {i}".format(i = new_codes)


class KirrURL(models.Model):

    url          = models.CharField(max_length = 220, )
    shortcode    = models.CharField(max_length = SHORTCODE_MAX, unique = True, blank = True)
    updated      = models.DateTimeField(auto_now= True)
    timestamp    = models.DateTimeField(auto_now_add= True)
    active       = models.BooleanField(default = True)

    #shortcode = models.CharField(max_length = 15, null = True) La base de datos vacia est bien
    #shortcode = models.CharField(max_length = 15, default = 'default')
    
    objects = KirrURL_Manager()
    #some_random = KirrURL_Manager()

    def save(self, *args, **kwargs):
        if not self.shortcode is None or self.shortcode == "":
            self.shortcode = create_Shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
    
    def __unicode__(self):
        return str(self.url)
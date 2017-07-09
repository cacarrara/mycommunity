from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

import googlemaps


class BusinessSegment(models.Model):
    name = models.CharField(_('Name'), max_length=250)

    class Meta:
        verbose_name = _('Segmento de Negócio')
        verbose_name_plural = _('Segmentos de Negócio')

    def __str__(self):
        return self.name


class Business(models.Model):
    SERVICE = 'service'
    TRADE = 'trade'
    BUSINESSES_TYPES = (
        (SERVICE, _('Service')),
        (TRADE, _('Trade')),
    )
    name = models.CharField(_('Name'), max_length=250, unique=True)
    address = models.CharField(_('Address'), max_length=250)
    latitude = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=10, decimal_places=7, blank=True, null=True)
    email = models.EmailField(_('E-Mail'))
    facebook_page = models.URLField(_('Facebook'), blank=True, null=True)
    twitter_profile = models.URLField(_('Twitter'), blank=True, null=True)
    linkedin_profile = models.URLField(_('LinkedIn'), blank=True, null=True)
    business_type = models.CharField(_('Type'), max_length=250, blank=False,
                                     null=False, default=TRADE,
                                     choices=BUSINESSES_TYPES)
    segment = models.ForeignKey(BusinessSegment, verbose_name=_('Segment'),
                                on_delete=models.CASCADE, blank=False, null=False,
                                related_name=u'businesses')

    class Meta:
        verbose_name = _('Negócio')
        verbose_name_plural = _('Negócios')

    def __str__(self):
        return "{} ({} - {})".format(self.name, self.segment, self.business_type)

    def _set_lat_lng(self):
        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        geocode = gmaps.geocode(self.address)
        if len(geocode) > 0:
            self.latitude = geocode[0]['geometry']['location']['lat']
            self.longitude = geocode[0]['geometry']['location']['lng']

    def save(self, *args, **kwargs):
        if self.address:
            self._set_lat_lng()
        return super(Business, self).save(*args, **kwargs)

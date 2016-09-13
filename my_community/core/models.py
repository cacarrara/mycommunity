from django.db import models
from django.utils.translation import ugettext_lazy as _


class BusinessSegment(models.Model):
    name = models.CharField(_('Name'), max_length=250)

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
    latitude = models.IntegerField(_('Latitude'), blank=True, null=True)
    longitude = models.IntegerField(_('Longitude'), blank=True, null=True)
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

    def __str__(self):
        return "{} ({} - {})".format(self.name, self.segment, self.business_type)

from tastypie.resources import ModelResource

from core.models import Business


class BusinessResource(ModelResource):
    class Meta:
        queryset = Business.objects.all()
        resource_name = 'business'

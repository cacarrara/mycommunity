from django.conf.urls import include, url

from core.api import BusinessResource
from core import views

business_resource = BusinessResource()

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^api/', include(business_resource.urls)),
    url(r'^business/add/$', views.business_add_view, name='add-business'),
]

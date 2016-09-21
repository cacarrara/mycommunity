from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^business/add/$', views.business_view, name='add-business'),
]

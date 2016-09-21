from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import TemplateView

from core.models import Business


class IndexView(TemplateView):
    template_name = 'index.html'


class BusinessAddView(CreateView):
    model = Business
    fields = ['name', 'address', 'email', 'facebook_page', 'twitter_profile', 'linkedin_profile', 'business_type',
              'segment']
    template_name = 'business_form.html'

    def get_success_url(self):
        return reverse('core:index')


index_view = IndexView.as_view()
business_add_view = BusinessAddView.as_view()

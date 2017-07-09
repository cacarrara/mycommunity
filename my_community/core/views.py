from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import TemplateView

from core.models import Business, BusinessSegment


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['segments'] = BusinessSegment.objects.all()
        return context


index_view = IndexView.as_view()


class BusinessAddView(CreateView):
    model = Business
    fields = ['name', 'address', 'email', 'facebook_page', 'twitter_profile',
              'linkedin_profile', 'business_type', 'segment']

    def get_success_url(self):
        return reverse('core:index')


business_add_view = BusinessAddView.as_view()

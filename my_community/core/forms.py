from django import forms

from core.models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'address', 'email', 'facebook_page',
                  'twitter_profile', 'linkedin_profile', 'business_type',
                  'segment']

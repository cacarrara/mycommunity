from unittest.mock import patch

from django.db import IntegrityError
from django.test import TestCase

from mixer.backend.django import mixer

from core.models import Business, BusinessSegment


class BusinessSegmentTestCase(TestCase):
    def setUp(self):
        mixer.cycle(5).blend(BusinessSegment)

    def test_string_format(self):
        b = BusinessSegment.objects.get(pk=1)
        self.assertEqual(b.name, b.__str__())


class BusinessTestCase(TestCase):
    def setUp(self):
        mixer.cycle(5).blend(Business, address='')

    def test_uniqueness(self):
        business = Business.objects.get(pk=1)
        new_business = Business(name=business.name)
        with self.assertRaises(IntegrityError):
            new_business.save()

    def test_string_format(self):
        b = Business.objects.get(pk=1)
        expected_str = "{} ({} - {})".format(b.name, b.segment, b.business_type)
        self.assertEqual(expected_str, b.__str__())

    @patch('core.models.googlemaps.Client.geocode')
    def test_set_lat_lng(self, mock_geocode):
        mock_geocode.return_value = [{
            'geometry': {
                'location': {'lat': 10, 'lng': 10}
            }
        }]
        b = mixer.blend(Business, address='')
        b.address = 'Sorocaba'
        b.save()
        self.assertEqual(b.latitude, 10)
        self.assertEqual(b.longitude, 10)


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """Get / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

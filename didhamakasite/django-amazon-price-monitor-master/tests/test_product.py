from django.test import TestCase

from price_monitor import app_settings
from price_monitor.models import Product


class ProductTest(TestCase):

    def test_set_failed_to_sync(self):
        asin = 'ASINASINASIN'
        p = Product.objects.create(asin=asin)
        self.assertIsNotNone(p)
        self.assertEqual(asin, p.asin)
        self.assertEqual(0, p.status)

        p.set_failed_to_sync()
        self.assertEqual(2, p.status)

    def test_get_image_urls(self):
        """Tests the Product.get_image_urls method."""

        # FIXME usually you would test a HTTP and a HTTPS setup but override_settings does not work with our app_settings (the setting does not get overwritten)

        # no images set
        p = Product.objects.create(
            asin='ASIN0000001',
        )
        self.assertEqual(3, len(p.get_image_urls()))
        self.assertTrue('small' in p.get_image_urls())
        self.assertTrue('medium' in p.get_image_urls())
        self.assertTrue('large' in p.get_image_urls())
        self.assertEqual(app_settings.PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN, p.get_image_urls()['small'])
        self.assertEqual(app_settings.PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN, p.get_image_urls()['medium'])
        self.assertEqual(app_settings.PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN, p.get_image_urls()['large'])

        # all images set
        p = Product.objects.create(
            asin='ASIN0000002',
            small_image_url='http://github.com/ponyriders/django-amazon-price-monitor/small.png',
            medium_image_url='http://github.com/ponyriders/django-amazon-price-monitor/medium.png',
            large_image_url='http://github.com/ponyriders/django-amazon-price-monitor/large.png',
        )
        self.assertEqual(3, len(p.get_image_urls()))
        self.assertTrue('small' in p.get_image_urls())
        self.assertTrue('medium' in p.get_image_urls())
        self.assertTrue('large' in p.get_image_urls())
        self.assertEqual(
            '{0}{1}'.format(app_settings.PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN, '/ponyriders/django-amazon-price-monitor/small.png'),
            p.get_image_urls()['small']
        )
        self.assertEqual(
            '{0}{1}'.format(app_settings.PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN, '/ponyriders/django-amazon-price-monitor/medium.png'),
            p.get_image_urls()['medium']
        )
        self.assertEqual(
            '{0}{1}'.format(app_settings.PRICE_MONITOR_AMAZON_SSL_IMAGE_DOMAIN, '/ponyriders/django-amazon-price-monitor/large.png'),
            p.get_image_urls()['large']
        )

    def test_get_detail_url(self):
        """Tests the get_detail_url method"""
        p = Product.objects.create(
            asin='ASIN0054321',
        )
        assert p.get_detail_url() == str(app_settings.PRICE_MONITOR_BASE_URL + '/#/products/ASIN0054321')

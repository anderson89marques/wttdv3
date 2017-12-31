from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Anderson Marques',
            cpf='12345678901',
            email='andersonoanjo18@gmail.com',
            phone='91-984593967'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
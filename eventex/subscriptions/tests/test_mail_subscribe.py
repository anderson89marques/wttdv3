from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Anderson Marques", cpf="01234567891",
                    email="andersonoanjo18@gmail.com", phone="91-984593967")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        """Subject must be 'Confirmação de inscrição'"""
        expect = "Confirmação de inscrição"

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """Email must come from 'contato@eventex.com.br'"""
        expect = "contato@eventex.com.br"

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ["contato@eventex.com.br", "andersonoanjo18@gmail.com"]
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Anderson Marques', '01234567891', 'andersonoanjo18@gmail.com', '91-984593967']    
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
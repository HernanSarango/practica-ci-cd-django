from django.test import TestCase
from django.urls import reverse


class InicioTest(TestCase):

    def test_pagina_inicio_responde_correctamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

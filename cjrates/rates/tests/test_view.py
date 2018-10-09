import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

# Initialize the APIClient() app

client = Client()


class RatesTest(TestCase):

    def test_get_rates(self):
        response = client.get(reverse('list_rates'))
        print('TESTING GET RATES')
        print(response)
        print(json.decoder(response))

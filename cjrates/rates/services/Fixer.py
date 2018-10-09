import requests
from rest_framework.parsers import json
from django.conf import settings


class Fixer(object):

    @staticmethod
    def perform():
        fixer_key = settings.FIXER_API_KEY
        fixer_endpoint = 'http://data.fixer.io/api/latest?access_key={}&format=1&symbols=MXN,USD'.format(fixer_key)
        response = requests.get(fixer_endpoint)
        response = json.loads(response.content.decode('utf-8'))
        mxn = response['rates']['MXN']
        usd = response['rates']['USD']
        rate = mxn/usd
        return rate

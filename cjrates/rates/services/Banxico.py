import requests
from django.conf import settings
import xml.etree.ElementTree as ET
from datetime import datetime

class Banxico(object):
    """
    Service object to retrieve the exchange rate from Banxico
    """
    @staticmethod
    def perform():
        banxico_token = settings.BANXICO_TOKEN
        headers = {'Accept': 'application/xml'}
        banxico_endpoint = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/sf43718/datos/2018-10-09/2018-10-09' \
                           '?token={}'.format(banxico_token)
        response = requests.get(banxico_endpoint, headers=headers)
        root = ET.fromstring(response.content)
        return root[0][0][0].text

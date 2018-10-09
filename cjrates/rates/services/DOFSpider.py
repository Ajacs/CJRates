
from bs4 import BeautifulSoup
import requests


class DOFSpider(object):

    @staticmethod
    def perform():
        site = requests.get('http://www.banxico.org.mx/tipcamb/tipCamMIAction.do')
        soup = BeautifulSoup(site.text, 'html.parser')
        dof_rate = soup.find('tr', attrs={'class': 'renglonNon'}).text.split()[2]
        return dof_rate


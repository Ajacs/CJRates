from . import DOFSpider


class DiarioOficialFederacion(object):
    """ Service object to retrieve the exchange rate from DOF"""

    @staticmethod
    def perform():
        """

        This needs to call the scrapper to get the information
        """
        DOFSpider().perform()
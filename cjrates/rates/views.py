from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .services import DOFSpider
from .services import Fixer
from .services import Banxico
from datetime import datetime

# Create your views here.


@api_view(['GET'])
def get_rates(request):
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'banxico': {
            'value': Banxico.perform(),
            'last_updated': last_updated
        },
        'fixer': {
            'value': Fixer.perform(),
            'last_updated': last_updated
        },
        'dof': {
            'value': DOFSpider.perform(),
            'last_updated': last_updated
        }
    }

    return Response({'rates': data}, status=status.HTTP_200_OK)

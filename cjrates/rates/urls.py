from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'rates/', views.get_rates, name='list_rates')
]
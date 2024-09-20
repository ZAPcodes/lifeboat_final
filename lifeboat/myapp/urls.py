from django.urls import path
from .views import receive_data, display_data

urlpatterns = [
    path('receive-data/', receive_data, name='receive_data'),
    path('display-data/', display_data, name='display_data'),
]

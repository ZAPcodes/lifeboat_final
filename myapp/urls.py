from django.urls import path
from .views import receive_data, display_data,get_latest_data,form

urlpatterns = [
    path('receive-data/', receive_data, name='receive_data'),
    path('form/display-data/', display_data, name='display_data'),
    path('latest-data/', get_latest_data, name='get_latest_data'),
    path('form/',form,name='form'),
]

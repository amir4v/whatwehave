from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('months/<int:year>', months),
    path('days/<int:month>', days),
    path('notes/<int:day>', notes),
]
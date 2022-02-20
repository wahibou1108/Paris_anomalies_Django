from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_q3'),
    path('index/',views.index, name='index_q3'),
    path('<int:type_anomalie_arrond_id>', views.detail, name='typeQ3'),
]
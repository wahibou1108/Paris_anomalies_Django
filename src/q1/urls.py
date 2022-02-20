from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_q1'),
    path('<int:id>', views.detail, name='arrondissement'),
]
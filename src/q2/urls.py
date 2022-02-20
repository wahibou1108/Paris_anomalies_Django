from django.urls import path
from unicodedata import name
from . import views

urlpatterns = [
    path('', views.index, name='index_q2'),
    path('<int:index>', views.detail, name='typeQ2'),
]
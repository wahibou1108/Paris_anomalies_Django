from django.http import HttpResponse
from django.shortcuts import render
from dans_ma_rue.models import *
from datetime import datetime

def index(request):

    return render(request,'index.html', {
        "date": datetime.today()}
        )
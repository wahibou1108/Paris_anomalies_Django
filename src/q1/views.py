
from django.shortcuts import render
from django.http import HttpResponse
from dans_ma_rue.models import *


def index(request):
    table = data.m_df_dicto()
    return render(request, 'q1/index.html', { 
        'table': table, 
         "date": datetime.today()
         })

def detail(request, id):
    ligne = data.m_df_ligne(id-1)
    table = data.m_df_dicto()
    c_img = "c_arrondissement_" + str(id) + ".png"
    h_img = "h_arrondissement_" + str(id) + ".png"
    return render(request, 'q1/arrondissement.html', { 
        "ligne"          : ligne,
        'id'              : id+1,
        "c_img"           : c_img,
        "h_img"           : h_img,
        'arrondissements' : list(range(1, 21)),
        'table'           : table,
         "date": datetime.today()
        })
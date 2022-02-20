from django.shortcuts import render
from django.http import HttpResponse
from dans_ma_rue.models import *


def index(request):
    d = df_3.m_df_dicto()
    donnee = df_3.m_df_ligne(10)
    
    return render(request, 'q3/index.html',{ 
        'donnee' : donnee,  
        'd' : d,
        'arrondissements'         : list(range(1, 21)),
        "date": datetime.today()
        })

def detail (request, type_anomalie_arrond_id):
    donnee = df_3.m_df_ligne(type_anomalie_arrond_id)
    d = df_3.m_df_dicto()
    h_img_q3_1 = 'h_anomalie_q3_graph_1__' + str(type_anomalie_arrond_id) + '.png' 
    h_img_q3_2 = 'h_anomalie_q3_graph_2__' + str(type_anomalie_arrond_id) + '.png' 
    h_img_q3_3 = 'h_anomalie_q3_graph_3__' + str(type_anomalie_arrond_id) + '.png' 
    h_img_q3_4 = 'h_anomalie_q3_graph_4__' + str(type_anomalie_arrond_id) + '.png' 
    h_img_q3_0 = 'h_anomalie_q3_graph_0__' + str(type_anomalie_arrond_id) + '.png' 
    min = donnee[type_anomalie_arrond_id][donnee[type_anomalie_arrond_id]['min']]
    max = donnee[type_anomalie_arrond_id][donnee[type_anomalie_arrond_id]['max']]
    q3_img = "type_anomalie_" + str(type_anomalie_arrond_id) + ".png"

    return render(request, 'q3/typeQ3.html', { 
        'donnee'                  : donnee,
        'd'                       : d,
        'type_anomalie_arrond_id' : type_anomalie_arrond_id -1,
        'h_img_q3_1'              : h_img_q3_1,
        'h_img_q3_2'              : h_img_q3_2,
        'h_img_q3_3'              : h_img_q3_3,
        'h_img_q3_4'              : h_img_q3_4,
        'arrondissements'         : list(range(1, 21)),
        'h_img_q3_0'              : h_img_q3_0,
        'min'                     : min,
        'max'                     : max,
         "date": datetime.today()
        })




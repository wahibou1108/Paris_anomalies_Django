from django.shortcuts import render
from django.http import HttpResponse
from dans_ma_rue.models import *

def index(request):
    table_2020 = df_2020.m_df_dicto()
    table_2021 = df_2021.m_df_dicto()
    return render(request,'q2/index.html', { 
        'table_2020' : table_2020,
        'table_2021' : table_2021,
        'dict_mois'  : DICT_MOIS,
        "date": datetime.today()        
        })

def detail(request, index):
    # table = df_2020.m_df_dicto()
    ligne_2020       = df_2020.m_df_ligne(index-1)
    table            = df_2020.m_df_dicto()
    h_img_2020       = 'h_anomalie_q2_2020_' + str(index) + '.png' 
    h_img_min_2020   = "h_anomalie_q2_2020_min_max_" + str(index-1) + '.png'

    ligne_2021       = df_2021.m_df_ligne(index-1)
    h_img_2021_sem_1 = 'h_anomalie_q2_sem_1_2021_' + str(index) + '.png' 
    h_img_2021_sem_2 = 'h_anomalie_q2_sem_2_2021_' + str(index) + '.png' 
    h_img_2021_sem_3 = 'h_anomalie_q2_sem_3_2021_' + str(index) + '.png' 
    h_img_min_2021   = "h_anomalie_q2_2021_min_max_" + str(index-1) + '.png'

    dict_mois = DICT_MOIS

    return render(request, 'q2/typeQ2.html', { 
        "ligne_2021"       : ligne_2021,
        "ligne_2020"       : ligne_2020,
        "table"            : table,
        "h_img_2020"       : h_img_2020,
        "h_img_2021_sem_1" : h_img_2021_sem_1,
        "h_img_2021_sem_2" : h_img_2021_sem_2,
        "h_img_2021_sem_3" : h_img_2021_sem_3,
        'dict_mois'        : dict_mois,
        "h_img_min_2020"   : h_img_min_2020,
        "h_img_min_2021"   : h_img_min_2021,
        "date": datetime.today()
        })

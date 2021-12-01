#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:33:18 2021

@author: eleonore
"""




import dash
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.graph_objs as go
import plotly.io as pio
import geopandas as gpd
from plotly.offline import plot
import pandas as pd
from urllib.request import urlopen
import plotly.express as px

comparison = pd.read_csv('data/comparison_baseline.csv')
comparison=comparison[0:18]
fig = px.bar(comparison, x="année", y=["comparison_depression","comparison_anxiete", "comparison_sommeil"],
               labels={'value':"différence de points de %",
                     "année": 'Date',
                     'variable':'indicateurs'
                 })




fig.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b>Différence de points de pourcentage par rapport à 2017<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)


plot(fig)


socio = pd.read_csv('data/depression_socio.csv')

socio_sexe= pd.melt(socio, id_vars=['année'], value_vars=['Homme','Femme'],
        var_name='sexe', value_name='Depression_sexe')

socio_professionel= pd.melt(socio, id_vars=['année'], value_vars=["Travail","Etudes","Chômage","Retraite ","Inactif"],
        var_name='situation_pro', value_name='Depression_professionel')

socio_situation= pd.melt(socio, id_vars=['année'], value_vars=["En entreprise", "Au chômage partiel",
                                                               "En arrêt de travail"],
        var_name='situtation_pro2', value_name='Depression_situation')

socio_professionel_g = px.scatter(socio_professionel, x="situation_pro",y="Depression_professionel", animation_frame="année",
            color="situation_pro", range_y=[0,50],
            labels={'Depression_professionel':"Symptômes dépressifs (%)",
                     "situation_pro": 'Catégorie',
                 })


socio_professionel_g.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Inidividus déclarant des symptomes dépressifs par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

#plot(socio_professionel_g)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:48:44 2021

@author: eleonore
"""

import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.graph_objs as go
import geopandas as gpd
from plotly.offline import plot
import pandas as pd
from urllib.request import urlopen
import io
from base64 import b64encode

all_data = pd.read_csv('data/coviprev.csv',
                       sep=';',decimal=',',header= 0,
                        encoding='utf-8')
annee = pd.read_csv('data/moyenne_annee.csv',
                       sep=';',decimal=',',header= 0,
                        encoding='utf-8')


comparison = pd.read_csv('data/comparison_baseline.csv')
comparison=comparison[0:18]

#### COMPARAISON 2017


fig_comparison = px.bar(comparison, x="année", y=["comparison_depression","comparison_anxiete", "comparison_sommeil"],
               labels={'value':"différence de points de %",
                     "année": 'Date',
                     'variable':'indicateurs'
                 },
               color_discrete_sequence= px.colors.sequential.Agsunset)




fig_comparison.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
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




fig_comparison.write_html(file='graphs/summary/bar_comparaison_2017.html')

fig_all = px.line(annee, x='année', y=['moyenne_depression', 'moyenne_anxiete',"moyenne_pbsommeil","moyenne_ps12mois"],
                    labels={
                    'variable':'Indicateurs',
                     "année": "Date",
                     "value": "Individus déclarant des symptômes (%)",
                     'moyenne_depression':'dépression',
                     'moyenne_anxiete':'anxiété',
                     'moyenne_pbsommeil':'problèmes de sommeil',
                     'moyenne_ps12mois':'pensées suicidaires'
                 },line_shape='spline',
                    color_discrete_sequence= px.colors.sequential.Agsunset)

fig_all.update_layout(
    font_color="darkblue",
    font_family="verdana",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
       title={
        'text': '<b>Prévalences et évolutions des indicateurs de santé mentale et des problèmes de sommeil<b>',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    #    legend=dict(
    # orientation="v",
    # yanchor="bottom",
    # y=1.02,
    # xanchor="right",
    # x=1,)
)


fig_all.add_hline(y=9.8, line_dash="dot",
              annotation_text="2017 baseline", 
              annotation_position="bottom right",line_color='rgb(75, 41, 145)',line_width=0.5)
fig_all.add_hline(y=13.5, line_dash="dot",
              annotation_text="2017 baseline", 
              annotation_position="bottom right",line_color= 'rgb(135, 44, 162)',line_width=0.5)

fig_all.add_hline(y=49.4, line_dash="dot",
              annotation_text="2017 baseline", 
              annotation_position="bottom right", line_color='rgb(192, 54, 157)', line_width=0.5)



fig_all.add_vrect(x0='mars 2020', x1='mai 2020', 
              annotation_text="Confinement 1", annotation_position="top left",
              fillcolor="blue", opacity=0.1, line_width=0)

fig_all.add_vrect(x0='novembre 2020', x1='décembre 2020', 
              annotation_text="Confinement 2", annotation_position="top left",
              fillcolor="blue", opacity=0.1, line_width=0)

fig_all.add_vrect(x0='mars 2021', x1='mai 2021', 
              annotation_text="Confinement 3", annotation_position="top left",
              fillcolor="blue", opacity=0.1, line_width=0)


fig_all.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-0.40,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

fig_all.write_html(file='graphs/summary/line_summary.html')
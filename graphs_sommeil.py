#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:39:38 2021

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


# LOAD DATA 
data = pd.read_csv('data/coviprev-age.csv',sep=';',decimal=',', encoding='utf-8')
data['date']=data.semaine.str[10:]

moyenne_age= pd.read_csv('data/moyenne_age.csv',sep=';',decimal=',', encoding='utf-8')
moyenne_sexe= pd.read_csv('data/moyenne_sexe.csv',sep=';',decimal=',', encoding='utf-8')
#SEX
data_sex = pd.read_csv('data/coviprev-sexe.csv',sep=';',decimal=',',encoding='utf-8')
data_sex['date']=data_sex.semaine.str[10:]



socios = pd.read_csv('data/sommeil-socio.csv',sep=';',decimal=',', encoding='utf-8')

socios_sexe= pd.melt(socios, id_vars=['année'], value_vars=['Homme','Femme'],
        var_name='sexe', value_name='Sommeil_sexe')

socios_professionel= pd.melt(socios, id_vars=['année'], value_vars=["Travail","Etudes","Chômage","Retraite","Inactif"],
        var_name='situation_pro', value_name='Sommeil_professionel')

socios_situation= pd.melt(socios, id_vars=['année'], value_vars=["En entreprise", "Au chômage partiel",
                                                               "En arrêt de travail"],
        var_name='situtation_pro2', value_name='Sommeil_situation')

covid_risques= pd.melt(socios, id_vars=['année'], value_vars=["risque_covid_non","risque_covid_oui"],
        var_name='risque', value_name='Sommeil_risque_covid')

covid_symptomess= pd.melt(socios, id_vars=['année'], value_vars=["symptomes_non","symptomes_oui"],
        var_name='symptomes', value_name='Sommeil_symptomes_covid')



# LINE GRAPH 1
line_graph_sleep = px.line(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_age, title='Évolution problèmes de sommeil par age', 
  # Set the x and y arguments
  x='année', y='pbsommeil', 
  # Ensure a separate line per country
  color='age',
   labels={'age':"Tranche d'âge",
                     "année": "Date",
                     "pbsommeil": "Individus déclarant des troubles du sommeil (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_sleep.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    yaxis_range=[40,90],
        title={
        'text': "<b>Évolution des troubles du sommeil dans le contexte de l’épidémie de Covid-19 (Tranche d'âge)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

line_graph_sleep.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

line_graph_sleep.update_xaxes(range=[1,18])

line_graph_sleep.write_html(file='graphs/sommeil/sommeil_line.html')



## LINE GRAPH 2 ANNOTATED
line_graph_sleep2 = px.line(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_age, title='Évolution problèmes de sommeil par age', 
  # Set the x and y arguments
  x='année', y='pbsommeil', 
  # Ensure a separate line per country
  color='age',
   labels={'age':"Tranche d'âge",
                     "année": "Date",
                     "pbsommeil": "Individus déclarant des troubles du sommeil (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_sleep2.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    yaxis_range=[40,90],
    font_size=12,
    plot_bgcolor='#ffffff',
        title={
        'text': "<b>Évolution des troubles du sommeil dans le contexte de l’épidémie de Covid-19 (Tranche d'âge)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

line_graph_sleep2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))
line_graph_sleep2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))


line_graph_sleep2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

  
line_graph_sleep2.add_annotation(font=dict(color="black",size=16),
                        x='avril 2020', y=40,
        text="1️⃣",
        showarrow=False,
        yshift=10)


line_graph_sleep2.add_annotation(font=dict(color="black",size=16),
                        x='novembre 2020', y=40,
            text="2️⃣",
            showarrow=False,
            yshift=10)


line_graph_sleep2.add_annotation(font=dict(color="black",size=16),
                        x='avril 2021', y=40,
            text="3️⃣",
            showarrow=False,
            yshift=10)


line_graph_sleep2.add_annotation(font=dict(color="black",size=16),
                        x='juillet 2021', y=40,
            text="💉",
            showarrow=False,
            yshift=10)

line_graph_sleep2.add_vrect(x0='mars 2020', x1='mai 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_sleep2.add_vrect(x0='novembre 2020', x1='décembre 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_sleep2.add_vrect(x0='mars 2021', x1='mai 2021', 
              fillcolor="blue", opacity=0.1, line_width=0)



line_graph_sleep2.write_html(file='graphs/sommeil/sommeil_line_annotated.html')

#### GRAPH SEXE


# Create the line graph
line_graph_sex_sommeil= px.scatter(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_sexe, title='Evolution problèmes de sommeil par sexe', 
  # Set the x and y arguments
  x='année', y='pbsommeil', 
  # Ensure a separate line per country
  color='sexe',
   labels={'sexe':"Sexe",
                     "année": "Date",
                     "pbsommeil": "Individus déclarant des troubles du sommeil (%)"
                 },
  color_discrete_sequence= px.colors.qualitative.Pastel[2:4])

line_graph_sex_sommeil.update_traces(marker={'size': 15})
line_graph_sex_sommeil.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    yaxis_range=[50,80],
    font_size=12,
    plot_bgcolor='#ffffff',
        title={
        'text': "<b>Évolution des troubles du sommeil dans le contexte de l’épidémie de Covid-19 (Sexe)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)


line_graph_sex_sommeil.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1.2,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

line_graph_sex_sommeil.update_xaxes(range=[1,18])

line_graph_sex_sommeil.write_html(file='graphs/sommeil/sommeil_sexe.html')

##### ANIMATIONS


####1
socio_professionel_gs = px.bar(socios_professionel, x="situation_pro",y="Sommeil_professionel", animation_frame="année",
            color="situation_pro", range_y=[40,80],
            labels={'Sommeil_professionel':"Troubles du sommeil (%)",
                     "situation_pro": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


socio_professionel_gs.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des troubles du sommeil par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

socio_professionel_gs.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

socio_professionel_gs.write_html(file='graphs/sommeil/sommeil_bar_socio_pro.html')

#####


covid_symptomes_gs = px.bar(covid_symptomess, x="symptomes",y="Sommeil_symptomes_covid", animation_frame="année",
            color="symptomes", range_y=[40,85],
            labels={'Sommeil_symptomes_covid':"Troubles du sommeil (%)",
                     "symptomes": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_symptomes_gs.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des troubles du sommeil par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

covid_symptomes_gs.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

covid_symptomes_gs.write_html(file='graphs/sommeil/sommeil_bar_covid_symptomes.html')

####risque


covid_risque_gs = px.bar(covid_risques, x="risque",y="Sommeil_risque_covid", animation_frame="année",
            color="risque",range_y=[40,85],
            labels={'Sommeil_risque_covid':"Troubles du sommeil (%)",
                     "risque": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_risque_gs.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des troubles du sommeil par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)


covid_risque_gs.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))


covid_risque_gs.write_html(file='graphs/sommeil/sommeil_bar_covid_risque.html')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:31:17 2021

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


##
socio = pd.read_csv('data/depression_socio.csv')

socio_sexe= pd.melt(socio, id_vars=['année'], value_vars=['Homme','Femme'],
        var_name='sexe', value_name='Depression_sexe')

socio_professionel= pd.melt(socio, id_vars=['année'], value_vars=["Travail","Etudes","Chômage","Retraite ","Inactif"],
        var_name='situation_pro', value_name='Depression_professionel')

socio_situation= pd.melt(socio, id_vars=['année'], value_vars=["En entreprise", "Au chômage partiel",
                                                               "En arrêt de travail"],
        var_name='situtation_pro2', value_name='Depression_situation')

covid_risque= pd.melt(socio, id_vars=['année'], value_vars=["risque_covid_non","risque_covid_oui"],
        var_name='risque', value_name='dep_risque_covid')

covid_symptomes= pd.melt(socio, id_vars=['année'], value_vars=["symptomes_non","symptomes_oui"],
        var_name='symptomes', value_name='dep_symptomes_covid')


# LINE GRAPH 1
line_graph_depression = px.line(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_age, title='<b>Évolution de symptômes dépressifs par âge durant les vagues Covid<b>', 
  # Set the x and y arguments
  x='année', y='depression', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     'année': 'Date',
                     "depression": "Individus déclarant des symptômes dépressifs (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_depression.update_yaxes(range=[0, 40])

line_graph_depression.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b>Évolution de symptômes dépressifs dans le contexte de l’épidémie de Covid-19 (Tranche d'âge)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },

)

line_graph_depression.update_xaxes(range=[1,18])

picker_style = {'float': 'left', 'margin': 'auto'}

line_graph_depression.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

line_graph_depression.write_html(file='graphs/depression/depression_line.html')



## LINE GRAPH 2 ANNOTATED

line_graph_depression2 = px.line(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_age, title='<b>Évolution de symptômes dépressifs par âge durant les vagues Covid<b>', 
  # Set the x and y arguments
  x='année', y='depression', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     'année': 'Date',
                     "depression": "Individus déclarant des symptômes dépressifs (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_depression2.update_yaxes(range=[0, 40])

line_graph_depression2.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b>Évolution de symptômes dépressifs dans le contexte de l’épidémie de Covid-19 (Tranche d'âge)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },

)


line_graph_depression2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))


line_graph_depression2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

  
line_graph_depression2.add_annotation(font=dict(color="black",size=16),
                        x='avril 2020', y=40,
        text="1️⃣",
        showarrow=False,
        yshift=10)


line_graph_depression2.add_annotation(font=dict(color="black",size=16),
                        x='novembre 2020', y=40,
            text="2️⃣",
            showarrow=False,
            yshift=10)


line_graph_depression2.add_annotation(font=dict(color="black",size=16),
                        x='avril 2021', y=40,
            text="3️⃣",
            showarrow=False,
            yshift=10)


line_graph_depression2.add_annotation(font=dict(color="black",size=16),
                        x='juillet 2021', y=40,
            text="💉",
            showarrow=False,
            yshift=10)

line_graph_depression2.add_vrect(x0='mars 2020', x1='mai 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_depression2.add_vrect(x0='novembre 2020', x1='décembre 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_depression2.add_vrect(x0='mars 2021', x1='mai 2021', 
              fillcolor="blue", opacity=0.1, line_width=0)



line_graph_depression2.write_html(file='graphs/depression/depression_line_annotated.html')

#### GRAPH SEXE 

line_graph_sex_depression= px.scatter(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_sexe, title='Évolution problèmes de dépression par sexe', 
  # Set the x and y arguments
  x='année', y='depression', 
   labels={'sexe':"Sexe",
                     "année": "Date",
                     "depression": "Individus déclarant des symptômes dépressifs (%)"
                 },
  # Ensure a separate line per country,
  color='sexe',
  range_y=[10,25],
  color_discrete_sequence= px.colors.qualitative.Pastel[2:4])


line_graph_sex_depression.update_xaxes(range=[0,19])
line_graph_sex_depression.update_traces(marker={'size': 15})

line_graph_sex_depression.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    #yaxis_range=[0,100],
    title={
        'text': "<b>Évolution de symptômes dépressifs dans le contexte de l’épidémie de Covid-19 (Sexe)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

line_graph_sex_depression.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

line_graph_sex_depression.write_html(file='graphs/depression/depression_sexe.html',auto_play=False)

##### ANIMATIONS

####1
socio_professionel_g = px.bar(socio_professionel, x="situation_pro",y="Depression_professionel", animation_frame="année",
            color="situation_pro", range_y=[0,50],
            labels={'Depression_professionel':"Symptômes dépressifs (%)",
                     "situation_pro": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


socio_professionel_g.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des symptomes dépressifs par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

socio_professionel_g.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

socio_professionel_g.write_html(file='graphs/depression/depression_bar_socio_pro.html',auto_play=False)
#####


covid_symptomes_g = px.bar(covid_symptomes, x="symptomes",y="dep_symptomes_covid", animation_frame="année",
            color="symptomes", range_y=[0,50],
            labels={'dep_symptomes_covid':"Symptômes dépressifs (%)",
                     "symptomes": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_symptomes_g.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des symptomes dépressifs par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

covid_symptomes_g.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

covid_symptomes_g.write_html(file='graphs/depression/depression_bar_covid_symptomes.html')
####risque


covid_risque_g = px.bar(covid_risque, x="risque",y="dep_risque_covid", animation_frame="année",
            color="risque", range_y=[0,50],
            labels={'dep_risque_covid':"Symptômes dépressifs (%)",
                     "risque": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_risque_g.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des symptomes dépressifs par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

covid_risque_g.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

covid_risque_g.write_html(file='graphs/depression/depression_bar_covid_risque.html',auto_play=False)
######

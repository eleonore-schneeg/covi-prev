#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:22:46 2021

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

socioa = pd.read_csv('data/anxiete-socio.csv', sep=';',decimal=',', encoding='utf-8')
socioa_sexe= pd.melt(socioa, id_vars=['année'], value_vars=['Homme','Femme'],
        var_name='sexe', value_name='Anxiete_sexe')

socioa_professionel= pd.melt(socioa, id_vars=['année'], value_vars=["Travail","Etudes","Chômage","Retraite","Inactif"],
        var_name='situation_pro', value_name='Anxiete_professionel')

socioa_situation= pd.melt(socioa, id_vars=['année'], value_vars=["En entreprise", "Au chômage partiel",
                                                               "En arrêt de travail"],
        var_name='situtation_pro2', value_name='Anxiete_situation')

covid_risquea= pd.melt(socioa, id_vars=['année'], value_vars=["risque_covid_non","risque_covid_oui"],
        var_name='risque', value_name='anxiete_risque_covid')

covid_symptomesa= pd.melt(socioa, id_vars=['année'], value_vars=["symptomes_non","symptomes_oui"],
        var_name='symptomes', value_name='anxiete_symptomes_covid')




# GRAPHIQUES INDICATEUR ANXIETE 


# LINE GRAPH 1
line_graph_anxiety = px.line(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_age, title="<b>Évolution de symptômes d'anxiété par âge durant les vagues Covid<b>", 
  # Set the x and y arguments
  x='année', y='anxiete', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     "année": 'Date',
                     "anxiete": "Individus déclarant des symptômes d'anxiété (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset,
  #error_y_minus='inf_anxiete',
  #error_y='sup_anxiete'
  )


line_graph_anxiety.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b>Évolution de symptômes d'anxiété dans le contexte de l’épidémie de Covid-19 (Tranche d'âge)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

picker_style = {'float': 'left', 'margin': 'auto'}

line_graph_anxiety.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

line_graph_anxiety.write_html(file='graphs/anxiete/anxiete_line.html')


## LINE GRAPH 2 ANNOTATED
line_graph_anxiety2 = px.line(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_age, title="<b>Évolution de symptômes d'anxiété par âge durant les vagues Covid<b>", 
  # Set the x and y arguments
  x='année', y='anxiete', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     "année": 'Date',
                     "anxiete": "Individus déclarant des symptômes d'anxiété (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset,
  #error_y_minus='inf_anxiete',
  #error_y='sup_anxiete'
  )


line_graph_anxiety2.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b>Évolution de symptômes d'anxiété dans le contexte de l’épidémie de Covid-19 (Tranche d'âge)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

picker_style = {'float': 'left', 'margin': 'auto'}

line_graph_anxiety2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

  
line_graph_anxiety2.add_annotation(font=dict(color="black",size=16),
                        x='avril 2020', y=40,
        text="1️⃣",
        showarrow=False,
        yshift=10)


line_graph_anxiety2.add_annotation(font=dict(color="black",size=16),
                        x='novembre 2020', y=40,
            text="2️⃣",
            showarrow=False,
            yshift=10)


line_graph_anxiety2.add_annotation(font=dict(color="black",size=16),
                        x='avril 2021', y=40,
            text="3️⃣",
            showarrow=False,
            yshift=10)


line_graph_anxiety2.add_annotation(font=dict(color="black",size=16),
                        x='juillet 2021', y=40,
            text="💉",
            showarrow=False,
            yshift=10)

line_graph_anxiety2.add_vrect(x0='mars 2020', x1='mai 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_anxiety2.add_vrect(x0='novembre 2020', x1='décembre 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_anxiety2.add_vrect(x0='mars 2021', x1='mai 2021', 
              fillcolor="blue", opacity=0.1, line_width=0)



line_graph_anxiety2.write_html(file='graphs/anxiete/anxiete_line_annotated.html')


#### GRAPH SEXE 


line_graph_sex_anxiete= px.scatter(
  # Set the appropriate DataFrame and title
  data_frame=moyenne_sexe, title="Évolution problèmes d'anxiété' par sexe", 
  # Set the x and y arguments
  x='année', y='anxiete', 
   labels={'sexe':"Sexe",
                     "année": "Date",
                     "anxiete": "Individus déclarant des symptômes d'anxiété' (%)"
                 },
  # Ensure a separate line per country
  color='sexe',
  color_discrete_sequence= px.colors.qualitative.Pastel[2:4])


line_graph_sex_anxiete.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    #yaxis_range=[0,100],
    title={
        'text': "<b>Évolution de symptômes d'anxiété dans le contexte de l’épidémie de Covid-19 (Sexe)<b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
line_graph_sex_anxiete.update_traces(marker={'size': 15})
line_graph_sex_anxiete.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

line_graph_sex_anxiete.write_html(file='graphs/anxiete/anxiete_sexe.html')

##### ANIMATIONS



####1
socio_professionel_ga = px.bar(socioa_professionel, x="situation_pro",y="Anxiete_professionel", animation_frame="année",
            animation_group="situation_pro",color="situation_pro", range_y=[0,50],
            labels={'Anxiete_professionel':"Symptômes anxieux (%)",
                     "situation_pro": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


socio_professionel_ga.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus déclarant des symptomes anxieux par situation professionnelle <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    transition= {'duration':1 }
)

socio_professionel_ga.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))


socio_professionel_ga.write_html(file='graphs/anxiete/anxiete_bar_socio_pro.html', auto_play=False)

import plotly.io as pio
pio.write_html(socio_professionel_ga, file='graphs/anxiete/index.html',auto_play=False)

#####


covid_symptomes_ga = px.bar(covid_symptomesa, x="symptomes",y="anxiete_symptomes_covid", animation_frame="année",
            color="symptomes", range_y=[0,50],
            labels={'anxiete_symptomes_covid':"Symptômes anxieux (%)",
                     "symptomes": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_symptomes_ga.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus présentant un risque de développer une forme grave de COVID-19 déclarant des symptomes anxieux <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)

covid_symptomes_ga.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

covid_symptomes_ga.write_html(file='graphs/anxiete/anxiete_bar_covid_symptomes.html',auto_play=False)

####risque


covid_risque_ga = px.bar(covid_risquea, x="risque",y="anxiete_risque_covid", animation_frame="année",
            color="risque", range_y=[0,50],
            labels={'anxiete_risque_covid':"Symptômes anxieux (%)",
                     "risque": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_risque_ga.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="verdana",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    title={
        'text': "<b> Individus ayant ou ayant eu des symptômes COVID et déclarant des symptomes d'anxiété <b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
)


covid_risque_ga.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.1,
                            y=-0.31,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))

covid_risque_ga.write_html(file='graphs/anxiete/anxiete_bar_covid_risque.html',auto_play=False)
######
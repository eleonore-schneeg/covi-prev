#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:56:48 2021

@author: eleonore
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:50:14 2021

@author: eleonore
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:28:13 2021
@author: eleonore
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:45:44 2021
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

import geopandas as gpd
from plotly.offline import plot
import pandas as pd
from urllib.request import urlopen



data = pd.read_csv('data/coviprev-age.csv',sep=';',decimal=',', encoding='utf-8')
data['date']=data.semaine.str[10:]

moyenne_age= pd.read_csv('data/moyenne_age.csv',sep=';',decimal=',', encoding='utf-8')

moyenne_sexe= pd.read_csv('data/moyenne_sexe.csv',sep=';',decimal=',', encoding='utf-8')

# interval de confiance 
data['inf_anxiete']=data['anxiete']-data['anxiete_inf']
data['sup_anxiete']=data['anxiete_sup']-data['anxiete']

data['inf_depression']=data['depression']-data['depression_inf']
data['sup_depression']=data['depression_sup']-data['depression']

data['inf_pbsommeil']=data['pbsommeil']-data['pbsommeil_inf']
data['sup_pbsommeil']=data['pbsommeil_sup']-data['pbsommeil']

# ANXIETY
# Create the line graph
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
    font_family="Uber Move Medium",
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


#### annotation

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
    font_family="Uber Move Medium",
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


# line_graph_anxiety2.add_vrect(x0='23-25 mars', x1='13-15 mai', 
#               annotation_text="Confinement 1", annotation_position="top left",
#               fillcolor="blue", opacity=0.1, line_width=0)

# line_graph_anxiety2.add_vrect(x0=' 4-6 nov.', x1=' 14-16 dec..', 
#               annotation_text="Confinement 2", annotation_position="top left",
#               fillcolor="blue", opacity=0.1, line_width=0)

# line_graph_anxiety2.add_vrect(x0=' 15-17 mars', x1=' 17-19 mai', 
#               annotation_text="Confinement 3", annotation_position="top left",
#               fillcolor="blue", opacity=0.1, line_width=0)

line_graph_anxiety2.add_vrect(x0='mars 2020', x1='mai 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_anxiety2.add_vrect(x0='novembre 2020', x1='décembre 2020', 
              fillcolor="blue", opacity=0.1, line_width=0)

line_graph_anxiety2.add_vrect(x0='mars 2021', x1='mai 2021', 
              fillcolor="blue", opacity=0.1, line_width=0)



confinement_1=[	'Vague 1 : 23-25 mars',	'Vague 7 : 13-15 mai']
confinement_2=[	'Vague 17 : 4-6 nov',	'Vague 19 : 14-16 dec']
confinement_3=[	'Vague 22 : 15-17 mars',	'Vague 24 : 17-19 mai']

# DEPRESSION

# Create the line graph
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
    font_family="Uber Move Medium",
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



#SLEEP
# Create the line graph
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
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    yaxis_range=[20,100],
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

#plot(line_graph_sleep)

#SEX
data_sex = pd.read_csv('data/coviprev-sexe.csv',sep=';',decimal=',',encoding='utf-8')
data_sex['date']=data_sex.semaine.str[10:]


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


line_graph_sex_sommeil.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
        yaxis_range=[20,100],
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
    font_family="Uber Move Medium",
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


####
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
    font_family="Uber Move Medium",
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

line_graph_sex_anxiete.add_annotation(dict(font=dict(color="black",size=10),
                            x=1,
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))



#####

all_data = pd.read_csv('data/coviprev.csv',
                       sep=';',decimal=',',header= 0,
                        encoding='utf-8')
annee = pd.read_csv('data/moyenne_annee.csv',
                       sep=';',decimal=',',header= 0,
                        encoding='utf-8')



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
    font_family="Uber Move Medium",
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




#######



region = pd.read_csv('data/coviprev-region.csv',sep=';',decimal=',', encoding='utf-8')

codes = pd.read_csv('data/metadata.csv',sep=';',decimal=',', encoding='utf-8')
codes = codes.rename(columns={'Code': 'reg'})
df= region.merge(codes, how='inner')

import json
with urlopen('https://france-geojson.gregoiredavid.fr/repo/regions.geojson') as response:
    region_j = json.load(response)
    
    
    
df['reg']=df['reg'].astype(int)
df['vague']=df.semaine.str[6:8]
df['vague']=df['vague'].astype(int)
df['date']=df.semaine.str[10:]


#######ANIMATIONS




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
    font_family="Uber Move Medium",
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
    font_family="Uber Move Medium",
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
    font_family="Uber Move Medium",
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
######

#######ANIMATIONS anxiete




socioa = pd.read_csv('data/anxiete-sociodemographie.csv', sep=';',decimal=',', encoding='utf-8')

socioa_sexe= pd.melt(socioa, id_vars=['année'], value_vars=['Homme','Femme'],
        var_name='sexe', value_name='Anxiete_sexe')

socioa_professionel= pd.melt(socioa, id_vars=['année'], value_vars=["Travail","Etudes","Chômage","Retraite","Inactif"],
        var_name='situation_pro', value_name='Anxiete_professionel')

socioa_situation= pd.melt(socioa, id_vars=['année'], value_vars=["En entreprise", "Au chômage partiel",
                                                               "En arrêt de travail"],
        var_name='situtation_pro2', value_name='Anxiete_situation')

covid_risquea= pd.melt(socioa, id_vars=['année'], value_vars=["risque_covid_non","risque_covid_oui"],
        var_name='risque', value_name='anxiete_risque_covid')

covid_symptomesa= pd.melt(socio, id_vars=['année'], value_vars=["symptomes_non","symptomes_oui"],
        var_name='symptomes', value_name='anxiete_symptomes_covid')



####1
socio_professionel_ga = px.bar(socioa_professionel, x="situation_pro",y="Anxiete_professionel", animation_frame="année",
            color="situation_pro", range_y=[0,50],
            labels={'Anxiete_professionel':"Symptômes anxieux (%)",
                     "situation_pro": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


socio_professionel_ga.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
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
)

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
    font_family="Uber Move Medium",
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
)

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
    font_family="Uber Move Medium",
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
)
######



socios = pd.read_csv('data/sommeil-socio.csv',sep=';',decimal=',', encoding='utf-8')

socios_sexe= pd.melt(socios, id_vars=['année'], value_vars=['Homme','Femme'],
        var_name='sexe', value_name='Sommeil_sexe')

socios_professionel= pd.melt(socios, id_vars=['année'], value_vars=["Travail","Etudes","Chômage","Retraite","Inactif"],
        var_name='situation_pro', value_name='Sommeil_professionel')

socios_situation= pd.melt(socios, id_vars=['année'], value_vars=["En entreprise", "Au chômage partiel",
                                                               "En arrêt de travail"],
        var_name='situtation_pro2', value_name='Sommeil_situation')

covid_risques= pd.melt(socioa, id_vars=['année'], value_vars=["risque_covid_non","risque_covid_oui"],
        var_name='risque', value_name='Sommeil_risque_covid')

covid_symptomess= pd.melt(socio, id_vars=['année'], value_vars=["symptomes_non","symptomes_oui"],
        var_name='symptomes', value_name='Sommeil_symptomes_covid')



####1
socio_professionel_gs = px.bar(socios_professionel, x="situation_pro",y="Sommeil_professionel", animation_frame="année",
            color="situation_pro", range_y=[0,50],
            labels={'Sommeil_professionel':"Troubles du sommeil (%)",
                     "situation_pro": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


socio_professionel_gs.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
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

#####


covid_symptomes_gs = px.bar(covid_symptomess, x="symptomes",y="Sommeil_symptomes_covid", animation_frame="année",
            color="symptomes", range_y=[0,50],
            labels={'Sommeil_symptomes_covid':"Troubles du sommeil (%)",
                     "symptomes": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_symptomes_gs.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
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

####risque


covid_risque_gs = px.bar(covid_risques, x="risque",y="Sommeil_risque_covid", animation_frame="année",
            color="risque", range_y=[0,50],
            labels={'Sommeil_risque_covid':"Troubles du sommeil (%)",
                     "risque": 'Catégorie',
                     "année":"Date"
                 },
            color_discrete_sequence= px.colors.sequential.Agsunset)


covid_risque_gs.update_layout(
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
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






#####
#BASELINE

comparison = pd.read_csv('data/comparison_baseline.csv')
comparison=comparison[0:18]
fig_comparison = px.bar(comparison, x="année", y=["comparison_depression","comparison_anxiete", "comparison_sommeil"],
               labels={'value':"différence de points de %",
                     "année": 'Date',
                     'variable':'indicateurs'
                 },
               color_discrete_sequence= px.colors.sequential.Agsunset)




fig_comparison.update_layout(
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




#####


app = dash.Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP], suppress_callback_exceptions = True,
                title='Dashboard #1',
                update_title='Loading healthcare data...')

app.css.config.serve_locally = True
#external_stylesheets=[dbc.themes.BOOTSTRAP]
#['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = app.server


app.css.config.serve_locally = True
app.scripts.config.serve_locally = True



sidebar = html.Div(
    [
        html.H1("Hippo", className="navbar-title"),
        html.H5("Santé Mentale 🐼", className="navbar-subtitle"),
        dbc.Nav(
            [
                dbc.NavLink("Accueil", href="/", active="exact",className="button"),
                dbc.NavLink("Évolution", href="/page-00", active="exact",className="button"),
                dbc.NavLink("Anxiété", href="/page-0", active="exact",className="button"),
                dbc.NavLink("Dépression", href="/page-1", active="exact",className="button"),
                dbc.NavLink("Sommeil", href="/page-2", active="exact",className="button"),
                dbc.NavLink("Carte", href="/page-3", active="exact",className="button"),
            ],
            vertical=True,
            pills=True,
            className="summary-navbar",
        ),
    ],
    className="navbar",
)


content = html.Div(id="page-content", children=[], className="content")

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Dashboard #1 CoviPrev 📈',className="content-title"),
                html.Div([
    dcc.Markdown('''
#### Une enquête pour suivre l’évolution des comportements et de la santé mentale pendant l'épidémie de COVID-19
>
> Depuis le 23 mars 2020, Santé publique France a lancé l'enquête CoviPrev en population générale afin de suivre l’évolution des comportements (gestes barrières, confinement, consommation d’alcool et de tabac, alimentation et activité physique) et de la santé mentale (bien-être, troubles).
>
_Source de l'enquête [suivant ce lien](https://www.santepubliquefrance.fr/etudes-et-enquetes/coviprev-une-enquete-pour-suivre-l-evolution-des-comportements-et-de-la-sante-mentale-pendant-l-epidemie-de-covid-19)._
''', className="content-warning")]),
 
html.Div(style={'width': '100%', 'display': 'inline-block','verticalAlign': 'top'}, children=[
    html.Div(dcc.Markdown('''
#### Objectifs ✔️
* Suivre l’adoption des mesures de protection et de la santé de la population pendant la période de confinement et de déconfinement 
* Recueillir les informations nécessaires à l’orientation et à l’ajustement des mesures de prévention
* Surveiller les inégalités de santé
* Capitaliser des connaissances utiles à la gestion de futures pandémies  
''', className='box'),style={'display': 'inline-block', "width": "50%", 'align-items': 'center','verticalAlign': 'top'}),

html.Div(dcc.Markdown('''
#### Méthodes 💡
* Enquêtes quantitatives répétées sur échantillons indépendants
* Questionnaires auto-administrés à remplir en ligne sur système Cawi (Computer Assisted Web Interview)
* Echantillons de 2 000 personnes de 18 ans et plus résidant en France métropolitaine recrutés par access panel (Access Panel BVA)
* Échantillonnage par quotas (sexe, âge, catégorie socio-professionnelles du répondant, région, catégorie d’agglomération) redressé sur le recensement général de la population 2016 
''', className='box'), style={'display': 'inline-block', "width": "50%",'align-items': 'center','verticalAlign': 'top'}),
                 
                ])
             ]
    elif pathname == "/page-00":
        return [
                html.H2("Évolutions des indicateurs depuis 2017",
                        className="content-title"),
                html.Div([
    dcc.Markdown('''
#### Comment peut-on mesurer l'évolution des indicateurs ?
>
> Différence de point de pourcentage entre une enqiuête de 2017 et l'enquête CoviPrev'
                                                                
_Baromètre de Santé publique France 2017 (BSpF)[ Disponible ici](https://www.santepubliquefrance.fr/etudes-et-enquetes/barometres-de-sante-publique-france/barometre-sante-2017)_''', className="content-warning")]),
                dcc.Graph(id='evolution',
                         figure=fig_comparison,className="content-graph"),
                ]    
                         
                       
    elif pathname == "/page-0":
        return [
                html.H2("Prévalences de l'anxiété dans le contexte de l’épidémie de Covid-19",
                        className="content-title"),
                html.Div([
                dcc.Markdown(''' 
                             ### Comment est mesurée l'anxiété dans l'enquête ?
                             _L’anxiété est mesurée par l’échelle HAD (Hospitality Anxiety and Depression scale ; score > 10)._''',className="content-warning")]),
                html.H4('Annoter le graphique avec les événements covid principaux 🖊️ :', className='content-paraf'),
                dcc.RadioItems(
                        id='events',
                        options=[{'label': 'Evénements covid', 'value': 'Evénements covid'},
                                  {'label': 'Non', 'value': 'Non'}],
                        value='Non', className='content-paraf'),
                dcc.Graph(id='bargraph1',
                         figure=line_graph_anxiety,className="content-graph"),
                 html.H4('Choisir une catégorie 🔎 :', className='content-paraf'),
                 dcc.Dropdown(
                        id='situation',
                        options=[{'label': 'Situation professionnelle', 'value': 'Situation professionnelle'},
                                  {'label': 'Symptômes COVID-19', 'value': 'symptômes COVID-19'},
                                  {'label': 'Risque covid', 'value': 'Risque covid'}],
                        value='Situation professionnelle',
                         placeholder='Sélectionner une catégorie',
         className='content-paraf'
         ),
                dcc.Graph(id='animation2',
                         figure=socio_professionel_g,className="content-graph"),
                dcc.Graph(id='bargraph2',
                         figure=line_graph_sex_anxiete,className="content-graph")
                
                ]    
                         
    elif pathname == "/page-1":
        return [
                html.H2('Prévalences de la dépression dans le contexte de l’épidémie de Covid-19',
                        className="content-title"),
                dcc.Markdown('''
                             ### Comment est mesurée la dépression dans l'enquête ?
                             _La dépression est mesurée par l’échelle HAD (Hospitality Anxiety 
                             and Depression scale ; score > 10._''', className="content-warning"),
                html.H4('Annoter le graphique avec les événements covid principaux 🖊️ :', className='content-paraf'),
                dcc.RadioItems(
                        id='events2',
                        options=[{'label': 'Evénements covid', 'value': 'Evénements covid'},
                                  {'label': 'Non', 'value': 'Non'},                 
                                  ],className='content-paraf'),
                dcc.Graph(id='bargraph1',
                         figure=line_graph_depression,className="content-graph"),
                html.H4('Choisir une catégorie 🔎 :', className='content-paraf'),
                 dcc.Dropdown(
                        id='situation',
                        options=[{'label': 'Situation professionnelle', 'value': 'Situation professionnelle'},
                                  {'label': 'Symptômes COVID-19', 'value': 'symptômes COVID-19'},
                                  {'label': 'Risque covid', 'value': 'Risque covid'}],
                        value='Situation professionnelle',
                         placeholder='Sélectionner une catégorie',
         className='content-paraf'
         ),
                dcc.Graph(id='animation1',
                         figure=socio_professionel_g,className="content-graph"),
                dcc.Graph(id='bargraph2',
                         figure=line_graph_sex_depression,className="content-graph"),
                
                ]
    elif pathname == "/page-2":
        return [
                html.H2('Prévalences des problèmes de sommeil dans le contexte de l’épidémie de Covid-19',
                        className="content-title"),
                dcc.Markdown('''
                             ### Comment sont mesurés les troubles du sommeil dans l'enquête ?
                             _La question posée était « Diriez-vous qu’au cours des 8 derniers jours, 
                             vous avez eu des problèmes de sommeil… ? ». Les personnes ayant répondu "un peu" 
                             ou "beaucoup" à la question ont été considérées 
                             comme ayant des problèmes de sommeil._''', className="content-warning"),
                html.H4('Annoter le graphique avec les événements covid principaux 🖊️ :', className='content-paraf'),
                dcc.Graph(id='bargraph3',
                         figure=line_graph_sleep,className="content-graph"),
                 html.H4('Choisir une catégorie 🔎 :', className='content-paraf'),
                 dcc.Dropdown(
                        id='situation',
                        options=[{'label': 'Situation professionnelle', 'value': 'Situation professionnelle'},
                                  {'label': 'Symptômes COVID-19', 'value': 'symptômes COVID-19'},
                                  {'label': 'Risque covid', 'value': 'Risque covid'}],
                        value='Situation professionnelle',
                         placeholder='Sélectionner une catégorie',
         className='content-paraf'
         ),
                dcc.Graph(id='animation3',
                         figure=socio_professionel_g,className="content-graph"),
                dcc.Graph(id='bargraph4',
                         figure=line_graph_sex_sommeil,className="content-graph")
                ]
    elif pathname == "/page-3":
        return [
                html.H2('Indicateurs de santé mentale par région dans le contexte de l’épidémie de Covid-19', className="content-title"),
                 html.H4('Varier la période 🗓 :', className='content-paraf'),
                dcc.Dropdown(
        id='demo-dropdown',
        options=[{"label": '23-25 mars 2020', "value": 1},
                 {"label": '30 mars-1 avr 2020', "value": 2},
                 {"label": '14-16 avr 2020', "value": 3},
                 {"label": '20-22 avr 2020', "value": 4},
                 {"label":'28-30 avr 2020', "value": 5},
                 {"label": '4-6 mai 2020', "value": 6},
                 {"label": '13-15 mai 2020', "value": 7},
                 {"label": '18-20 mai 2020', "value": 8},
                 {"label": '27-29 mai 2020', "value": 9},
                 {"label": '8-10 juin 2020', "value": 10},
                 {"label": '22-24 juin 2020', "value": 11},
                 {"label": '6-8 juillet 2020', "value": 12},
                 {"label": '20-22 juillet 2020', "value": 13},
                 {"label": '24-26 août 2020', "value": 14},
                 {"label": '21-23 sept 2020', "value": 15},
                 {"label": '19-21 oct 2020', "value": 16},
                    {"label": '4-6 nov 2020', "value": 17},
                    {"label": '23-25 nov 2020', "value": 18},
                    {"label": '14-16 dec 2020', "value": 19},
                    {"label": '18-20 janv 2021', "value": 20},
                    {"label": '15-17 fév 2021', "value": 21},
                    {"label": '15-17 mars 2021', "value": 22},
                    {"label": '21-23 avril 2021', "value": 23},
                    {"label": '17-19 mai 2021', "value": 24},
                    {"label": '21-28 juin 2021', "value": 25},
                    {"label": '15-21 juillet 2021', "value": 26},
                    {"label": '31 août-7 sept 2021', "value": 27},
                    {"label": '28 sept- 5 oct 2021', "value": 28}],

                value=1,
                placeholder='Select date',
          className='content-paraf'
         ),
                html.Div([
    dcc.Graph(id='graph-with-slider',className="content-graph"),
    dcc.Graph(id='graph-with-slider2', className="content-graph"),
    dcc.Graph(id='graph-with-slider3', className="content-graph")

]),

                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    Output('graph-with-slider', 'figure'),
    Output('graph-with-slider2', 'figure'),
    Output('graph-with-slider3', 'figure'),
    Input('demo-dropdown', 'value'),
    suppress_callback_exceptions=True)
def update_figure(value):
    filtered_df = df[df.vague == value]

    fig = px.choropleth_mapbox(
    filtered_df,
    geojson=region_j,
    locations='reg',
    color='anxiete',
    featureidkey="properties.code",
    color_continuous_scale='purples',
    hover_name='Libellé',
    mapbox_style='carto-positron',
    zoom=4,
    center={'lat': 47, 'lon': 2},
    opacity=0.8,
      labels={'anxiete':"anxiété (%)",
                     "reg": 'code région',
                 }
   )
    
    # Define layout specificities
    fig.update_layout(
    coloraxis_colorbar={
        'title':'anxiété (%)'  
    },
    title={
        'text': f'Prévalence de symptômes anxieux par région {filtered_df.date.unique()}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue"
    )
    
    fig.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.01,
                            y=-0.08,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="paper",
                            yref="paper"
                           ))

    fig2 = px.choropleth_mapbox(
    filtered_df,
    geojson=region_j,
    locations='reg',
    color='depression',
    featureidkey="properties.code",
    color_continuous_scale='PuRd',
    hover_name='Libellé',
    mapbox_style='carto-positron',
    zoom=4,
    center={'lat': 47, 'lon': 2},
    opacity=0.8,
          labels={'depression':"dépression (%)",
                     "reg": 'code région',
                 }
   )
    
    # Define layout specificities
    fig2.update_layout(
    coloraxis_colorbar={
        'title':'dépression (%)'  
    },
    title={
        'text': f'Prévalence de symptômes dépressifs par région {filtered_df.date.unique()}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue",)

    fig2.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.01,
                            y=-0.08,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="paper",
                            yref="paper"
                           ))


    fig3 = px.choropleth_mapbox(
    filtered_df,
    geojson=region_j,
    locations='reg',
    color='pbsommeil',
    featureidkey="properties.code",
    color_continuous_scale='Peach',
    hover_name='Libellé',
    mapbox_style='carto-positron',
    zoom=4,
    center={'lat': 47, 'lon': 2},
    opacity=0.8,
              labels={'pbsommeil':"troubles du sommeil (%)",
                     "reg": 'code région',
                 }
   )
    
    # Define layout specificities
    fig3.update_layout(
    coloraxis_colorbar={
        'title':"troubles du sommeil (%)"},
    title={
        'text': f'Prévalence des troubles du sommeil par région {filtered_df.date.unique()}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font_color="darkblue",
    title_font_color="darkblue",
    font_family="Uber Move Medium",
    legend_title_font_color="darkblue",
)
    fig3.add_annotation(dict(font=dict(color="black",size=10),
                            x=1.01,
                            y=-0.08,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="paper",
                            yref="paper"
                           ))

    return fig, fig2, fig3

@app.callback(
    Output('bargraph1','figure'),
    Input('events','value'))
def annotation_figure(value):

    fig4=line_graph_anxiety
    fig5=line_graph_anxiety2
  
        
    if value == 'Evénements covid':
        return fig5
    
    else:                   
        return fig4

@app.callback(
    Output('animation1','figure'),
    Input('situation','value'))
def annotation_figure(value):
        
    if value == 'Situation professionnelle':
        return socio_professionel_g
    
    if value == 'Risque covid':
    
        return covid_risque_g
    
    else:                   
        return covid_symptomes_g

@app.callback(
    Output('animation2','figure'),
    Input('situation','value'))
def annotation_figure(value):
        
    if value == 'Situation professionnelle':
        return socio_professionel_ga
    
    if value == 'Risque covid':
    
        return covid_risque_ga
    
    else:                   
        return covid_symptomes_ga

@app.callback(
    Output('animation3','figure'),
    Input('situation','value'))
def annotation_figure(value):
        
    if value == 'Situation professionnelle':
        return socio_professionel_gs
    
    if value == 'Risque covid':
    
        return covid_risque_gs
    
    else:                   
        return covid_symptomes_gs


if __name__=='__main__':
    app.run_server(debug=True)
    
    

    
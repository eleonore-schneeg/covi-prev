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
import plotly.io as pio
import geopandas as gpd
from plotly.offline import plot
import pandas as pd
from urllib.request import urlopen



data = pd.read_csv('data/coviprev-age.csv',sep=';',decimal=',', encoding='utf-8')


# ANXIETY
# Create the line graph
line_graph_anxiety = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data, title='<b>Évolution de symptômes dépressifs par âge durant les vagues Covid<b>', 
  # Set the x and y arguments
  x='semaine', y='anxiete', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     "semaine": 'Semaine',
                     "anxiete": "Individus déclarant des symptômes d'anxiété (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_anxiety.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family='Arial',
    title_font_color="darkblue",
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
line_graph_anxiety.update_xaxes(title_font_family="Arial")
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



# DEPRESSION

# Create the line graph
line_graph_depression = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data[5:139], title='<b>Évolution de symptômes dépressifs par âge durant les vagues Covid<b>', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     "semaine": 'Semaine',
                     "depression": "Individus déclarant des symptômes dépressifs (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_depression.update_yaxes(range=[0, 40])

line_graph_depression.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family='Arial',
    title_font_color="darkblue",
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
line_graph_depression.update_xaxes(title_font_family="Arial")
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
  data_frame=data[5:139], title='Évolution problèmes de sommeil par age', 
  # Set the x and y arguments
  x='semaine', y='pbsommeil', 
  # Ensure a separate line per country
  color='age',
   labels={'age':"Tranche d'âge",
                     "semaine": "Semaine",
                     "pbsommeil": "Individus déclarant des troubles du sommeil (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_sleep.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
    #yaxis_range=[0,100],
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



#plot(line_graph_sleep)

#SEX
data_sex = pd.read_csv('data/coviprev-sexe.csv',sep=';',decimal=',',encoding='utf-8')
# Create the line graph
line_graph_sex_sommeil= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:55], title='Evolution problèmes de sommeil par sexe', 
  # Set the x and y arguments
  x='semaine', y='pbsommeil', 
  # Ensure a separate line per country
  color='sexe',
   labels={'sexe':"Sexe",
                     "semaine": "Semaine",
                     "pbsommeil": "Individus déclarant des troubles du sommeil (%)"
                 },
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_sex_sommeil.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=12,
    plot_bgcolor='#ffffff',
        #yaxis_range=[0,100],
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
                            y=-1,
                            showarrow=False,
                            text='<b>Source: Hippo.vision 🦛 </b>',
                            textangle=0,
                            xref="x domain",
                            yref="y domain"
                           ))



line_graph_sex_depression= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:55], title='Évolution problèmes de dépression par sexe', 
  # Set the x and y arguments
  x='semaine', y='depression', 
   labels={'sexe':"Sexe",
                     "semaine": "Semaine",
                     "depression": "Individus déclarant des symptômes dépressifs (%)"
                 },
  # Ensure a separate line per country
  color='sexe',
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_sex_depression.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
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
line_graph_sex_anxiete= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:55], title="Évolution problèmes d'anxiété' par sexe", 
  # Set the x and y arguments
  x='semaine', y='anxiete', 
   labels={'sexe':"Sexe",
                     "semaine": "Semaine",
                     "anxiete": "Individus déclarant des symptômes d'anxiété' (%)"
                 },
  # Ensure a separate line per country
  color='sexe',
  line_shape='spline',
  color_discrete_sequence= px.colors.sequential.Agsunset)


line_graph_sex_anxiete.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
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


fig_all = px.line(all_data, x='semaine', y=['depression', 'anxiete',"pbsommeil"],
                    labels={
                    'variable':'Indicateurs',
                     "semaine": "Semaine",
                     "value": "Individus déclarant des symptômes (%)",
                     'depression':'dépression',
                     'anxiete':'anxiété',
                     'pbsommeil':'troubles du sommeil'
                 },line_shape='spline',
                    color_discrete_sequence= px.colors.sequential.Agsunset)

fig_all.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
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
       legend=dict(
    orientation="v",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1,
))


fig_all.add_hline(y=18, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right",line_color='rgb(75, 41, 145)',line_width=0.5)
fig_all.add_hline(y=15, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right",line_color= 'rgb(135, 44, 162)',line_width=0.5)

fig_all.add_hline(y=60, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right", line_color='rgb(192, 54, 157)', line_width=0.5)


confinement_1=[	'Vague 1 : 23-25 mars',	'Vague 7 : 13-15 mai']
confinement_2=[	'Vague 17 : 4-6 nov',	'Vague 19 : 14-16 dec']
confinement_3=[	'Vague 22 : 15-17 mars',	'Vague 24 : 17-19 mai']

fig_all.add_vrect(x0='Vague 1 : 23-25 mars', x1='Vague 7 : 13-15 mai', 
              annotation_text="Confinement 1", annotation_position="top left",
              fillcolor="blue", opacity=0.1, line_width=0)

fig_all.add_vrect(x0='Vague 17 : 4-6 nov', x1='Vague 19 : 14-16 dec..', 
              annotation_text="Confinement 2", annotation_position="top left",
              fillcolor="blue", opacity=0.1, line_width=0)

fig_all.add_vrect(x0='Vague 22 : 15-17 mars', x1='Vague 24 : 17-19 mai', 
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
#######


app = dash.Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP], suppress_callback_exceptions = True,
                title='Dashboard #1',
                update_title='Loading healthcare data...')


#external_stylesheets=[dbc.themes.BOOTSTRAP]
#['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = app.server


app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H5("CoviPrev", className="display-4"),
        html.Hr(),
        html.P(
            "Santé Mentale 🐼 ", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Accueil", href="/", active="exact"),
                dbc.NavLink("Anxiété", href="/page-0", active="exact"),
                dbc.NavLink("Dépression", href="/page-1", active="exact"),
                dbc.NavLink("Sommeil", href="/page-2", active="exact"),
                dbc.NavLink("Carte", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

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
                html.H1('Dashboard #1 CoviPrev 📈',
                        style={'textAlign':'center','margin-bottom':50}),
                html.Div([
    dcc.Markdown('''
#### Une enquête pour suivre l’évolution des comportements et de la santé mentale pendant l'épidémie de COVID-19
>
> Depuis le 23 mars 2020, Santé publique France a lancé l'enquête CoviPrev en population générale afin de suivre l’évolution des comportements (gestes barrières, confinement, consommation d’alcool et de tabac, alimentation et activité physique) et de la santé mentale (bien-être, troubles).
>
_Source de l'enquête [suivant ce lien](https://www.santepubliquefrance.fr/etudes-et-enquetes/coviprev-une-enquete-pour-suivre-l-evolution-des-comportements-et-de-la-sante-mentale-pendant-l-epidemie-de-covid-19)._
''', style={'textAlign':'left','margin-left': 100,'width': '80%', 'margin-bottom':50} )]),
 
html.Div([dcc.Markdown('''
#### Objectifs ✔️
* Suivre l’adoption des mesures de protection et de la santé de la population pendant la période de confinement et de déconfinement 
* Recueillir les informations nécessaires à l’orientation et à l’ajustement des mesures de prévention
* Surveiller les inégalités de santé
* Capitaliser des connaissances utiles à la gestion de futures pandémies  
''', style={'textAlign':'left','margin-left': 100,'width': '80%','margin-bottom':50} )]),

html.Div([dcc.Markdown('''
#### Méthodes 💡
* Enquêtes quantitatives répétées sur échantillons indépendants
* Questionnaires auto-administrés à remplir en ligne sur système Cawi (Computer Assisted Web Interview)
* Echantillons de 2 000 personnes de 18 ans et plus résidant en France métropolitaine recrutés par access panel (Access Panel BVA)
* Échantillonnage par quotas (sexe, âge, catégorie socio-professionnelles du répondant, région, catégorie d’agglomération) redressé sur le recensement général de la population 2016 
''', style={'textAlign':'left','margin-left': 100,'margin-bottom':50} ),
                 # dcc.Graph(id='bargraph0',
                 #         figure=fig_all,
                 #             style={'textAlign':'center','margin-left': 80,'width': '90%'}),
                ])]
                       
    elif pathname == "/page-0":
        return [
                html.H2("Prévalences de l'anxiété dans le contexte de l’épidémie de Covid-19",
                        style={'textAlign':'center','margin-left': 100, 'margin-bottom':50}),
                html.Div([
                dcc.Markdown(''' _L’anxiété est mesurée par l’échelle HAD (Hospitality Anxiety and Depression scale ; score > 10)._''', style={'textAlign':'left','margin-left': 100,'width': '80%'} ),
                dcc.Graph(id='bargraph1',
                         figure=line_graph_anxiety,style={'textAlign':'center','margin-left': 80,'width': '90%'}),
                dcc.Graph(id='bargraph2',
                         figure=line_graph_sex_anxiete,style={'textAlign':'center','margin-left': 80,'width': '90%'})
                ])
                ]    
                         
    elif pathname == "/page-1":
        return [
                html.H2('Prévalences de la dépression dans le contexte de l’épidémie de Covid-19',
                        style={'textAlign':'center','margin-left': 100, 'margin-bottom':50}),
                dcc.Markdown(''' _La dépression est mesurée par l’échelle HAD (Hospitality Anxiety and Depression scale ; score > 10._''', style={'textAlign':'left','margin-left': 100,'width': '80%'} ),
                dcc.Graph(id='bargraph1',
                         figure=line_graph_depression,style={'textAlign':'center','margin-left': 80,'width': '90%'}),
                dcc.Graph(id='bargraph2',
                         figure=line_graph_sex_depression,style={'textAlign':'center','margin-left': 80,'width': '90%'})
                ]
    elif pathname == "/page-2":
        return [
                html.H2('Prévalences des problèmes de sommeil dans le contexte de l’épidémie de Covid-19',
                        style={'textAlign':'center','margin-left': 100,'margin-bottom':50}),
                html.H1('   '),
                dcc.Markdown('''_La question posée était « Diriez-vous qu’au cours des 8 derniers jours, vous avez eu des problèmes de sommeil… ? ». Les personnes ayant répondu "un peu" ou "beaucoup" à la question ont été considérées comme ayant des problèmes de sommeil._''', style={'textAlign':'left','margin-left': 100,'width': '80%'} ),
                dcc.Graph(id='bargraph3',
                         figure=line_graph_sleep,style={'textAlign':'center','margin-left': 80,'width': '90%'}),
                dcc.Graph(id='bargraph4',
                         figure=line_graph_sex_sommeil,style={'textAlign':'center','margin-left': 80,'width': '90%'})
                ]
    elif pathname == "/page-3":
        return [
                html.H2('Indicateurs de santé mentale par région dans le contexte de l’épidémie de Covid-19', style={'textAlign':'center','margin-left': 80,'width': '90%','margin-bottom':50}),
                 html.H4('Varier la période 🗓 :', style={'textAlign':'left','margin-left': 100}),
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
                    {"label": '32 août-7 sept 2021', "value": 27},
                    {"label": '28 sept- 5 oct 2021', "value": 28}],

                value=1,
                placeholder='Select date',
         style = {"width": "200px",'position': 'center','margin-left': 50}
         ),
                html.Div([
    dcc.Graph(id='graph-with-slider', style={'textAlign':'center','margin-left': 100,'width': '80%'}),
    dcc.Graph(id='graph-with-slider2', style={'textAlign':'center','margin-left': 100,'width': '80%'}),
    dcc.Graph(id='graph-with-slider3', style={'textAlign':'center','margin-left': 100,'width': '80%'})

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
        'text': f'Prévalence de symptômes anxieux par région {filtered_df.semaine.unique()}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
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
        'text': f'Prévalence de symptômes dépressifs par région {filtered_df.semaine.unique()}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    })

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
        'text': f'Prévalence des troubles du sommeil par région {filtered_df.semaine.unique()}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
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





if __name__=='__main__':
    app.run_server(debug=True)
    
    
    
    
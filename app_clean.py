#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:52:57 2021

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
import io
from base64 import b64encode


exec(open("graphs_anxiete.py").read())
exec(open("graphs_sommeil.py").read())
exec(open("graphs_depression.py").read())
exec(open("graphs_summary.py").read())
exec(open("graphs_map.py").read())



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
    
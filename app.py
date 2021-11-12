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

data = pd.read_csv('data/coviprev-age.csv',sep=';',decimal=',')


# ANXIETY
# Create the line graph
line_graph_anxiety = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data[5:79], title='Évolution anxiete par age', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  # Ensure a separate line per country
  color='age')

#plot(line_graph_anxiety)



# DEPRESSION

# Create the line graph
line_graph_depression = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data[5:79], title='Évolution de symptômes dépressifs par âge durant les vagues Covid', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     "semaine": "Vague",
                     "depression": "% d'individus déclarant des symptômes dépressifs"
                 })


line_graph_depression.update_yaxes(range=[0, 40])

line_graph_depression.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff'
)
line_graph_depression.update_xaxes(title_font_family="Arial")
picker_style = {'float': 'left', 'margin': 'auto'}


#plot(line_graph_depression)




#SLEEP
# Create the line graph
line_graph_sleep = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data[5:79], title='Évolution problèmes de sommeil par age', 
  # Set the x and y arguments
  x='semaine', y='pbsommeil', 
  # Ensure a separate line per country
  color='age')


line_graph_sleep.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff',
    yaxis_range=[0,100]
)



#plot(line_graph_sleep)

#SEX
data_sex = pd.read_csv('data/coviprev-sexe.csv',sep=';',decimal=',')
# Create the line graph
line_graph_sex_sommeil= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:32], title='Evolution problèmes de sommeil par sexe', 
  # Set the x and y arguments
  x='semaine', y='pbsommeil', 
  # Ensure a separate line per country
  color='sexe')


line_graph_sex_sommeil.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff',
        yaxis_range=[0,100]
)

line_graph_sex_depression= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:32], title='Évolution problèmes de dépression par sexe', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  labels={
                    'age':"Tranche d'âge"},
  # Ensure a separate line per country
  color='sexe')


line_graph_sex_depression.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff',
        yaxis_range=[0,100]
)


picker_style = {'float': 'left', 'margin': 'auto'}
#####

all_data = pd.read_csv('data/coviprev.csv',
                       sep=';',decimal=',',header= 0,
                        encoding= 'unicode_escape')


fig_all = px.line(all_data, x='semaine', y=['depression', 'anxiete',"pbsommeil"],
                    labels={
                    'variable':'Indicateurs',
                     "semaine": "Vague",
                     "value": "% d'individus déclarant des symptômes"
                 })

fig_all.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Droid Sans",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff',
)

fig_all.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

fig_all.add_hline(y=20, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right",line_color='blue')
fig_all.add_hline(y=25, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right",line_color='red')

fig_all.add_hline(y=60, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right", line_color='green')


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



#######


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])


server = app.server
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
            "Santé Publique France", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Accueil", href="/", active="exact"),
                dbc.NavLink("Dépression", href="/page-1", active="exact"),
                dbc.NavLink("Sommeil", href="/page-2", active="exact"),
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
                html.H1('',
                        style={'textAlign':'center'}),
                html.Div([
    dcc.Markdown('''
#### Dashboard #1 CoviPrev 📈

**Une enquête pour suivre l’évolution des comportements et de la santé mentale pendant l'épidémie de COVID-19**
>
> Depuis le 23 mars 2020, Santé publique France a lancé l'enquête CoviPrev en population générale afin de suivre l’évolution des comportements (gestes barrières, confinement, consommation d’alcool et de tabac, alimentation et activité physique) et de la santé mentale (bien-être, troubles).
>

_Source de l'enquête [suivant ce lien](https://www.santepubliquefrance.fr/etudes-et-enquetes/coviprev-une-enquete-pour-suivre-l-evolution-des-comportements-et-de-la-sante-mentale-pendant-l-epidemie-de-covid-19)._

''', style={'textAlign':'center','margin-left': 100,'width': '80%'} )]),
 
html.Div([dcc.Markdown('''
#### Objectifs ✔️
* Suivre l’adoption des mesures de protection et de la santé de la population pendant la période de confinement et de déconfinement 
* Recueillir les informations nécessaires à l’orientation et à l’ajustement des mesures de prévention
* Surveiller les inégalités de santé
* Capitaliser des connaissances utiles à la gestion de futures pandémies  

''', style={'textAlign':'left','margin-left': 100,'width': '80%'} )]),

html.Div([dcc.Markdown('''
#### Méthodes 💡
* Enquêtes quantitatives répétées sur échantillons indépendants
* Questionnaires auto-administrés à remplir en ligne sur système Cawi (Computer Assisted Web Interview)
* Echantillons de 2 000 personnes de 18 ans et plus résidant en France métropolitaine recrutés par access panel (Access Panel BVA)
* Échantillonnage par quotas (sexe, âge, catégorie socio-professionnelles du répondant, région, catégorie d’agglomération) redressé sur le recensement général de la population 2016 


''', style={'textAlign':'left','margin-left': 90,'width': '80%'} ),
                 dcc.Graph(id='bargraph',
                         figure=fig_all,
                             style={'textAlign':'center','margin-left': 100,'width': '90%'}),
                ])]
                       
                               
    elif pathname == "/page-1":
        return [
                html.H1('Données relatives aux signes dépressifs',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=line_graph_depression,style={'textAlign':'center','margin-left': 100,'width': '80%'}),
                dcc.Graph(id='bargraph',
                         figure=line_graph_sex_depression,style={'textAlign':'center','margin-left': 100,'width': '80%'})
                ]
    elif pathname == "/page-2":
        return [
                html.H1('Données relatives aux troubles du sommeil',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=line_graph_sleep,style={'textAlign':'center','margin-left': 100,'width': '80%'}),
                dcc.Graph(id='bargraph',
                         figure=line_graph_sex_sommeil,style={'textAlign':'center','margin-left': 100,'width': '80%'})
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__=='__main__':
    app.run_server(debug=True)
    
    
    
    

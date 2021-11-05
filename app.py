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
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

data = pd.read_csv('data/coviprev-age.csv',sep=';',decimal=',')


# ANXIETY
# Create the line graph
line_graph_anxiety = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data[5:79], title='Evolution anxiete par age', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  # Ensure a separate line per country
  color='age')

#plot(line_graph_anxiety)



# DEPRESSION

# Create the line graph
line_graph_depression = px.line(
  # Set the appropriate DataFrame and title
  data_frame=data[5:79], title='Evolution de symptômes dépressifs par âge durant les vagues Covid', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  # Ensure a separate line per age
  color='age',
  labels={
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
  data_frame=data[5:79], title='Evolution problèmes de sommeil par age', 
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
    plot_bgcolor='#ffffff'
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
    plot_bgcolor='#ffffff'
)

line_graph_sex_depression= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:32], title='Evolution problèmes de dépression par sexe', 
  # Set the x and y arguments
  x='semaine', y='depression', 
  # Ensure a separate line per country
  color='sexe')


line_graph_sex_depression.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff'
)


picker_style = {'float': 'left', 'margin': 'auto'}
#####

all_data = pd.read_csv('data/coviprev.csv',
                       sep=';',decimal=',',header= 0,
                        encoding= 'unicode_escape')


fig_all = px.line(all_data, x='semaine', y=['depression', 'anxiete',"pbsommeil"],
                    labels={
                     "semaine": "Vague",
                     "depression": "% d'individus déclarant des symptômes"
                 })

fig_all.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff'
)
picker_style = {'float': 'left', 'margin': 'auto'}


#######

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


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
            "Une enquête pour suivre l’évolution des comportements et de la santé mentale pendant l'épidémie de COVID-19", className="lead"
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
                html.H1('Evolution de tous les marqueurs',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=fig_all)
                ]
    elif pathname == "/page-1":
        return [
                html.H1('Données relatives aux signes dépressifs',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=line_graph_depression),
                dcc.Graph(id='bargraph',
                         figure=line_graph_sex_depression)
                ]
    elif pathname == "/page-2":
        return [
                html.H1('Données relatives aux troubles du sommeil',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=line_graph_sleep),
                dcc.Graph(id='bargraph',
                         figure=line_graph_sex_sommeil)
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
    
    
    
    
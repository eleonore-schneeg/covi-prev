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


import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

data = pd.read_csv('/Users/eleonore/OneDrive - Imperial College London/Health Data Today/Data/France//CoviPrev/coviprev-age.csv',sep=';',decimal=',')


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
    font_size=10
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


#plot(line_graph_sleep)

#SEX
data_sex = pd.read_csv('/Users/eleonore/OneDrive - Imperial College London/Health Data Today/Data/France//CoviPrev/coviprev-sexe.csv',sep=';',decimal=',')
# Create the line graph
line_graph_sex= px.line(
  # Set the appropriate DataFrame and title
  data_frame=data_sex[0:32], title='Evolution problèmes de sommeil par sexe', 
  # Set the x and y arguments
  x='semaine', y='pbsommeil', 
  # Ensure a separate line per country
  color='sexe')


line_graph_sex.update_layout(
    font_family="Arial",
    font_color="darkblue",
    title_font_family="Arial",
    title_font_color="darkblue",
    legend_title_font_color="darkblue",
    font_size=10,
    plot_bgcolor='#ffffff'
)

line_graph_sex.update_xaxes(title_font_family="Arial")
picker_style = {'float': 'left', 'margin': 'auto'}



#plot(line_graph_sex)

#####
#APP#
#####

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


colors = {
    'background': '#ffffff',
    'text': '#00008B'
}

line_graph_depression.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(style={'backgroundColor': colors['background']},className='row', children=[
    html.H1("Dashboard données dépression"),
    dcc.Dropdown(),
    html.Div(style={'backgroundColor': colors['background']},children=[
        dcc.Graph(id="graph1",figure=line_graph_depression, style={'display': 'inline-block','backgroundColor': colors['background']}),
        dcc.Graph(id="graph2",figure=line_graph_sex ,style={'display': 'inline-block','backgroundColor': colors['background']})
    ]),
    html.H1("Dashboard données dépression"),
    dcc.Dropdown(),
    html.Div(id='my-output')
])



if __name__ == '__main__':
    app.run_server(debug=True, port=9000)

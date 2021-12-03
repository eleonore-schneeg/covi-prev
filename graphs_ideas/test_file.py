#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:47:22 2021

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


# GRAPHIQUES INDICATEUR ANXIETE 


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

buffer = io.StringIO()
line_graph_anxiety.write_html(buffer, file='anxiete_line.html')

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()
#plot(line_graph_anxiety)

app = dash.Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP], suppress_callback_exceptions = True,
                title='Dashboard #1',
                update_title='Loading healthcare data...')

app.layout = html.Div([

    dcc.Graph(id='bargraph1',
                         figure=line_graph_anxiety),
        html.A(
        html.Button("Download HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="plotly_graph.html"
    )
])


if __name__=='__main__':
    app.run_server(debug=True)
    

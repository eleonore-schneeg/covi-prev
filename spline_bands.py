#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:26:07 2021

@author: eleonore
"""


import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from plotly.offline import plot

def line(error_y_mode=None, **kwargs):
    """Extension of `plotly.express.line` to use error bands."""
    ERROR_MODES = {'bar','band','bars','bands',None}
    if error_y_mode not in ERROR_MODES:
        raise ValueError(f"'error_y_mode' must be one of {ERROR_MODES}, received {repr(error_y_mode)}.")
    if error_y_mode in {'bar','bars',None}:
        fig = px.line(**kwargs)
    elif error_y_mode in {'band','bands'}:
        if 'error_y' not in kwargs:
            raise ValueError(f"If you provide argument 'error_y_mode' you must also provide 'error_y'.")
        figure_with_error_bars = px.line(**kwargs)
        fig = px.line(**{arg: val for arg,val in kwargs.items() if arg != 'error_y'})
        for data in figure_with_error_bars.data:
            x = list(data['x'])
            y_upper = list(data['y'] + data['error_y']['array'])
            y_lower = list(data['y'] - data['error_y']['array'] if data['error_y']['arrayminus'] is None else data['y'] - data['error_y']['arrayminus'])
            color = f"rgba({tuple(int(data['line']['color'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))},.3)".replace('((','(').replace('),',',').replace(' ','')
            fig.add_trace(
                go.Scatter(
                    x = x+x[::-1],
                    y = y_upper+y_lower[::-1],
                    fill = 'toself',
                    line_shape='spline',
                    fillcolor = color,
                    line = dict(
                        color = 'rgba(255,255,255,0)'
                    ),
                    hoverinfo = "skip",
                    showlegend = False,
                    legendgroup = data['legendgroup'],
                    xaxis = data['xaxis'],
                    yaxis = data['yaxis'],
                )
            )
        # Reorder data as said here: https://stackoverflow.com/a/66854398/8849755
        reordered_data = []
        for i in range(int(len(fig.data)/2)):
            reordered_data.append(fig.data[i+int(len(fig.data)/2)])
            reordered_data.append(fig.data[i])
        fig.data = tuple(reordered_data)
    return fig

data = pd.read_csv('data/coviprev-age.csv',sep=';',decimal=',', encoding='utf-8')
data['date']=data.semaine.str[10:]

# interval de confiance 
data['inf_anxiete']=data['anxiete']-data['anxiete_inf']
data['sup_anxiete']=data['anxiete_sup']-data['anxiete']

data['inf_depression']=data['depression']-data['depression_inf']
data['sup_depression']=data['depression_sup']-data['depression']

data['inf_pbsommeil']=data['pbsommeil']-data['pbsommeil_inf']
data['sup_pbsommeil']=data['pbsommeil_sup']-data['pbsommeil']

fig = line(
        data_frame=data, title="<b>Évolution de symptômes d'anxiété par âge durant les vagues Covid<b>", 
  # Set the x and y arguments
  x='date', y='anxiete', 
  # Ensure a separate line per age
  color='age',
  labels={'age':"Tranche d'âge",
                     "date": 'Date',
                     "anxiete": "Individus déclarant des symptômes d'anxiété (%)"
                 },
  line_shape='spline',
        error_y_minus='inf_anxiete',
        error_y='sup_anxiete',
        error_y_mode = 'band',
    )

plot(fig)


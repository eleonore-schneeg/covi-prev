#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:46:57 2021

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

#LOAD DATA

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

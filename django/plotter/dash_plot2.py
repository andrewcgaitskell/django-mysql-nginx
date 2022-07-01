#import libraries
from os import name
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from .models import LimitOwnerships
import pymysql
import pandas as pd
from django.db import connection

def dash_plotly_plot():
    """
    Output: Figure object
    """
    query = str(LimitOwnerships.objects.all().query)
    df = pd.read_sql_query(query, connection)
    
    #Create graph object Figure object with data
    fig = go.Scatter(x=df['user_id'], y=df['limit_id'], mode='markers',name='markers')
    
    #Update layout for graph object Figure
    fig.update_layout(title_text = 'Dash_Plot2',
                      xaxis_title = 'X_Axis',
                      yaxis_title = 'Y_Axis')
    
    return fig


#Create DjangoDash applicaiton
app = DjangoDash(name='DashPlot2')

#Configure app layout
app.layout = html.Div([
                html.Div([
                    html.Div([                 
                    dcc.Graph(id = 'dash_plot_2', 
                              animate = True, 
                              style={"backgroundColor": "#FFF0F5"})])
                        ])])


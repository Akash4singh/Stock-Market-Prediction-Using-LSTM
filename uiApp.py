import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from collections import Counter
import unicodedata
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from random import randint
import threading
import pandas as pd
import os
from tkinter import filedialog
from tkinter import *
import base64
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import main_mlp0 as main

#import main

app = dash.Dash()

im1='https://lh4.googleusercontent.com/l89WZtMBMv3Vfn-cG91JxQahQ7X2UrpIxmUfv9lZCP_YNmXTJgFlE7cHY7AolgWNhNikVWNm4UDLCo-3x9ZJ=w1366-h695-rw'
im2='https://lh6.googleusercontent.com/V4ADKW0RIwKe923Vujsjs0bikIdF0PJMgxmX_S1SfS0Bqznjjz0Apziz0YRGsEUeF9EzDVdfUsGVbfKe_rdN=w1366-h695'
im3='https://lh6.googleusercontent.com/AuM___ZcQRDSmKvqYTjekVctEsTdxBag-ZCyDneXbMoPGXIyAdFoNnwrk3qkxR071whEM4BXUjvA71Acn42k=w1366-h695-rw'
im4='https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png'
im5='https://seeklogo.com/images/S/spyder-logo-68D7CF8B2C-seeklogo.com.png'
im6='https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Plotly-logo-01-square.png/220px-Plotly-logo-01-square.png'
im7= 'http://www.commzgate.com/assets/img/commzgate_cloud_api.png'
im8='https://cdn0.iconfinder.com/data/icons/trending-tech/94/artificial_intelligence-512.png'
im9 ='https://cdn-images-1.medium.com/max/1200/1*lkqc68a6b7_TLALs5fmI6A.png'

df=pd.read_csv("all_stocks_5yr.csv")
company = df['Name'].unique()
        

app.layout = html.Div([
    html.H1(children="Stock Market's Price Movement Prediction Using LSTM Model", style={'marginBottom': '12px','background-color' :'#FA8072','color' : 'white'}),
    html.Div(children = [html.Img(src=im1,style={'width': '33%', 'marginLeft': 'auto', 'marginRight': 'auto','marginBottom': '25'}),
                         html.Img(src=im2,style={'width': '33%', 'marginLeft': 'auto', 'marginRight': 'auto','marginBottom': '25'}),
                         html.Img(src=im3,style={'width': '33%', 'marginLeft': 'auto', 'marginRight': 'auto','marginBottom': '25'}),
                         ]),
    dcc.Dropdown(id='page-2-dropdown',options=[{'label': i, 'value': i} for i in company]),
    html.Button(id='submit-button', n_clicks=0, children='Submit', 
    style={'marginTop': 15, 'marginBottom': 25}),
    html.Div(id='my-div')
], style={'textAlign': 'center'})

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks'),
     Input(component_id='page-2-dropdown', component_property= 'value')])
def update_output_div(n_clicks,company):
    if n_clicks > 0:
        val = main.main(company)
        im1 = app.get_asset_url('out.png')
        #print(im1)
    return  html.Div([html.H1(children=val, style={'marginBottom': '12px'}),html.Img(src=f'assets/out'+company+'.png',style={'width': '40%', 'marginLeft': 'auto', 'marginRight': 'auto'})])
        
        
if __name__ == '__main__':
    app.run_server(port=3040)
        

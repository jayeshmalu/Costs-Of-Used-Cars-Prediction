import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from flask import Flask, send_from_directory
import pandas as pd
import numpy as np
from numpy import arange
import joblib
import zipfile

external_scripts = ['']
external_stylesheets = [
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

data = pd.read_csv('Mapping Data.csv')
car_model_list = list(data['Name'].unique())
Location_list = list(data['Location'].unique())

server = Flask(__name__)

app = dash.Dash(server=server, external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

Kilometers_Driven_input = html.Div(
    [
        dbc.Label("Kilometers Driven", html_for="example-Kilometers_Driven"),
        dbc.Input(type="number", id="example-Kilometers_Driven",min=0 ,step=0.1 ,placeholder="Enter Kilometers Driven"),
    ],
    className="mb-3",
)


Owner_Type_input = html.Div(
    [
        dbc.Label("Owner Type", html_for="example-Mileage"),
        dcc.Dropdown(
            id='Owner_Type',
            options=[
                {'label': 'First', 'value': '1'},
                {'label': 'Second', 'value': '2'},
                {'label': 'Third', 'value': '3'},
                {'label': 'Fourth & Above', 'value': '4'},
            ],
            placeholder="Select Owner Type",
            clearable=False,
        ),
    ],
    className="mb-3",
)

Mileage_input = html.Div(
    [
        dbc.Label("Mileage (km per l/kg)", html_for="example-Mileage"),
        dbc.Input(type="number", id="example-Mileage",min=0,step=0.1 ,placeholder="Enter Mileage (km per l/kg)"),
    ],
    className="mb-3",
)

Engine_input = html.Div(
    [
        dbc.Label("Engine (in CC)", html_for="example-Engine"),
        dbc.Input(type="number", id="example-Engine",min=0,step=0.1 ,placeholder="Enter Engine Capacity (in CC)"),
    ],
    className="mb-3",
)

Power_input = html.Div(
    [
        dbc.Label("Power (in BHP)", html_for="example-Power"),
        dbc.Input(type="number", id="example-Power",min=0,step=0.1 ,placeholder="Enter Power (in BHP)"),
    ],
    className="mb-3",
)

Seats_input = html.Div(
    [
        dbc.Label("Seats", html_for="example-Seats"),
        dbc.Input(type="number", id="example-Seats",min=0 ,placeholder="Enter Number of Seats"),
    ],
    className="mb-3",
)

New_Price_input = html.Div(
    [
        dbc.Label("New Price (in Lakh)", html_for="example-New_Price"),
        dbc.Input(type="number", id="example-New_Price",min=0,step=0.1 ,placeholder="Enter New Price (in Lakh)"),
    ],
    className="mb-3",
)

Used_Years_input = html.Div(
    [
        dbc.Label("Used Years", html_for="example-Used_Years"),
        dbc.Input(type="number", id="example-Used_Years",min=0,step=0.1 ,placeholder="Enter Used Years"),
    ],
    className="mb-3",
)

Car_Model_Name_input = html.Div(
    [
        dbc.Label("Car & Model Name", html_for="example-Car_Model_Name"),
        dcc.Dropdown(
            id='Car_Model_Name',
            options=[
                {'label': i, 'value': i} for i in sorted(car_model_list)
            ],
            placeholder="Select Car & Model Name",
            clearable=False,
        ),
    ],
    className="mb-3",
)

Location_input = html.Div(
    [
        dbc.Label("Location", html_for="example-Location"),
        dcc.Dropdown(
            id='Location',
            options=[
                {'label': i, 'value': i} for i in sorted(Location_list)
            ],
            placeholder="Select Location",
            clearable=False,
        ),
    ],
    className="mb-3",
)

Transmission_input = html.Div(
    [
        dbc.Label("Transmission", html_for="example-Transmission"),
        dcc.Dropdown(
            id='Transmission',
            options=[
                {'label': 'Manual', 'value': '1'},
                {'label': 'Automatic', 'value': '0'},
            ],
            placeholder="Select Transmission",
            clearable=False,
        ),
    ],
    className="mb-3",
)

Fuel_Type_input = html.Div(
    [
        dbc.Label("Fuel Type", html_for="example-Fuel_Type"),
        dcc.Dropdown(
            id='Fuel_Type',
            options=[
                {'label': 'Petrol', 'value': 'Petrol'},
                {'label': 'Diesel', 'value': 'Diesel'},
                {'label': 'LPG', 'value': 'LPG'},
                {'label': 'CNG', 'value': 'CNG'},
            ],
            placeholder="Select Fuel Type",
            clearable=False,
        ),
    ],
    className="mb-3",
)

form = dbc.Form(
    id="form",
    children=[
        Kilometers_Driven_input,
        Owner_Type_input,
        Mileage_input,
        Engine_input,
        Power_input,
        Seats_input,
        New_Price_input,
        Used_Years_input,
        Car_Model_Name_input,
        Location_input,
        Transmission_input,
        Fuel_Type_input,
        
        dbc.Button("Predict", color="primary"),
    ],className="ml-5 mr-5 pl-5 pr-5",
    #inline=True,
)


## Layout Scripts ##
app.layout = html.Div(children=[
    ########## Navbar ##########
    dbc.NavbarSimple(
        id="button",
        brand="Used Car Price Prediction",
        color="#667292",
        # dark=True,
        className="shadow-sm mb-1 bg-white",


        style={"paddingTop": 0, "paddingBottom": 0, "font-weight": "600",
            "marginLeft":0,   "font-size": 30, 'fontFamily': ' Tahoma, sans-serif'},
    ),

    html.Div([form, html.Div([html.Div("Predicted Price : "),html.Div(id="output",className='ml-1')],className="row ml-5 mr-5 pl-5 mt-2",style={"font-weight": "500","font-size": 20,"color":"red"})],className="mt-3 ml-5 mr-5 pl-5 pr-5"),
    
        html.Div([
        html.B(["© Jayesh Malu"], style={
               "marginLeft": "3%", "color": "#5C7191", "fontSize": 13}),
    ], style={"background-color": "#F7F7F7", "padding": 10,'marginTop':10}),



], style={"overflow": "hidden", "background-color": "#F9FDFF"})

@app.callback(
    Output("output", "children"),
    Input("form", "n_submit"),
    State("example-Kilometers_Driven", "value"),
    State("Owner_Type", "value"),
    State("example-Mileage", "value"),
    State("example-Engine", "value"),
    State("example-Power", "value"),
    State("example-Seats", "value"),
    State("example-New_Price", "value"),
    State("example-Used_Years", "value"),
    State("Car_Model_Name", "value"),
    State("Location", "value"),
    State("Transmission", "value"),
    State("Fuel_Type", "value"),    
    prevent_initial_call=True
)
def handle_submit(n_submit,example_Kilometers_Driven,Owner_Type,example_Mileage,example_Engine,example_Power,example_Seats,example_New_Price,example_Used_Years,Car_Model_Name,Location,Transmission,Fuel_Type):
    
    
    
    if (example_Kilometers_Driven is None) or (Owner_Type is None) or (example_Mileage is None) or (example_Engine is None) or (example_Power is None) or (example_Seats is None) or (example_New_Price is None) or (example_Used_Years is None) or (Car_Model_Name is None) or (Location is None) or (Transmission is None) or (Fuel_Type is None):
        prediction = "Please fill all inputs"

    else:
        e_Name = data[data['Name']==Car_Model_Name].iloc[0]['e_Name']
        e_Name1 = data[data['Name']==Car_Model_Name].iloc[0]['e_Name1']
        e_Name2 = data[data['Name']==Car_Model_Name].iloc[0]['e_Name2']

        Location = data[data['Location']==Location].iloc[0]['e_Location']

        Fuel_Type_Petrol =0
        Fuel_Type_Diesel =0
        Fuel_Type_LPG =0
        Fuel_Type_CNG =0

        if Fuel_Type == 'Petrol':
            Fuel_Type_Petrol =1
        if Fuel_Type == 'Diesel':
            Fuel_Type_Diesel =1
        if Fuel_Type == 'LPG':
            Fuel_Type_LPG =1
        if Fuel_Type == 'CNG':
            Fuel_Type_CNG =1
            
        
        archive = zipfile.ZipFile('car_price_prediction_model.zip', 'r')
        #imgfile = archive.open('img_01.png')
        et_model1 = archive.open('car_price_prediction_model.pkl')

        et_model = joblib.load(et_model1)

#         et_model = joblib.load('car_price_prediction_model.pkl')

        #prediction = np.round(et_model.predict([[41000,1.00,19.67,1582,126,5,12.5,6,496,63,179,10,1,0,1,0,0]]))
        prediction = np.round(et_model.predict([[example_Kilometers_Driven,Owner_Type,example_Mileage,example_Engine,example_Power,example_Seats,example_New_Price,example_Used_Years,e_Name,e_Name1,e_Name2,Location,Transmission,Fuel_Type_CNG,Fuel_Type_Diesel,Fuel_Type_LPG,Fuel_Type_Petrol]]),2)
        prediction = str(list(prediction)[0]) + ' Lakhs'
    return prediction

if __name__ == '__main__':
    app.run_server(debug=True)

from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import temp_main as temp_main
import csv
from datetime import datetime, date
import DataGeneration
from flask import Flask, render_template, make_response
import subprocess
import os
from hal import hal_dc_motor as dc_motor

file_location = os.path.realpath(__file__)
directory = os.path.dirname(file_location)
file_path = os.path.join(directory, "main.py").replace("\\", "/")
process = None
app = Flask(__name__)
csvfile = "Alldatas.csv"
state = -1
line = 3
past_date = None

def start_code():
    global process
    if process is None:
        process = subprocess.Popen(["python", file_path])
    # get the date when the code is started
    global past_date
    if not past_date:
        past_date = datetime.now()
        DataGeneration.WriteFieldNames()
    else:
        current_date = datetime.now()
        if current_date.day != past_date.day:
            DataGeneration.save_to_csv(past_date.strftime("%Y-%m-%d"))
            past_date = current_date
            DataGeneration.WriteFieldNames()

def stop_code():
    global process
    dc_motor.init()
    dc_motor.set_motor_speed(0)
    if process is not None:
        process.terminate()
        process = None

@app.route('/', methods=["GET", "POST"])
def temp_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('home.html')

@app.route('/index.html')
def index_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('index.html')

@app.route('/temperature.html')
def temperature_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('temperature.html')

@app.route('/humidity.html')
def humidity_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('humidity.html')

@app.route('/ec.html')
def ec_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('ec.html')

@app.route('/ph.html')
def ph_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('ph.html')

@app.route('/light.html')
def light_html():
    global line
    line = DataGeneration.LatestLine(csvfile)
    return render_template('light.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity, EC, PH, Light]
    global line
    ListofDatas = DataGeneration.ReadLine(csvfile,line)
    if ListofDatas:
        line += 1
        data = ListofDatas
        response = make_response(json.dumps(data))
    else:
        response = make_response(json.dumps([]))
    response.content_type = 'application/json'
    return response

def get_latest_data():
    #if date reaches the next day create a new csv file
    global past_date
    current_date = datetime.now()
    if past_date and current_date.day != past_date.day:
        DataGeneration.save_to_csv(past_date.strftime("%Y-%m-%d"))
        past_date = current_date
        DataGeneration.WriteFieldNames()
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) > 1:
            latest_row = data[-1]
            return latest_row
        else:
            return None

@app.route('/data_current', methods=["GET"])
def data_current():
    latest_data = get_latest_data()
    if latest_data:
        data = latest_data
        response = make_response(json.dumps(data))
    else:
        response = make_response(json.dumps([]))
    response.content_type = 'application/json'
    return response

@app.route('/switch-state', methods=["GET", "POST"])
def switch_state():
    global state
    state *= -1
    if state == 1:
        start_code()
    if state == -1:
        stop_code()
    response_switch = make_response(json.dumps(state))
    return response_switch

@app.route('/get-switch-state', methods=["GET"])
def get_switch_state():
    global state
    response = make_response(json.dumps(state))
    return response


if __name__ == "__main__":
    app.run(debug=True)
import random as rng
import csv
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime,date
csvfile = "src/Alldatas.csv"

def DataGeneration(Temperature, Humidity, Moisture_sensor, Potentiometer, LDR):
    Time = (time.time() + 28800000) * 1000
    WriteData([Time, Temperature, Humidity, Moisture_sensor, Potentiometer, LDR])
    return [Time, Temperature, Humidity, Moisture_sensor, Potentiometer, LDR]

def WriteFieldNames():
    with open(csvfile,"w") as file:
        writer = csv.writer(file)
        Data = ["Time", "Temperature", "Humidity", "Moisture_sensor", "Potentiometer", "LDR"]
        writer.writerow(Data)
    return
def WriteData(Datas):
    if Datas[3]:
        Datas[3] = 1.0
    else:
        Datas[3] = 0.0
    with open(csvfile, 'a', newline="") as Data:
        print(Datas)
        writer = csv.writer(Data)
        writer.writerow(Datas)
    return
def ReadLine(csvfile,line):
    data = []
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(line - 1):
            next(reader)
        for i in next(reader):
            data.append(float(i))      
    return data

def LatestLine(csvfile):
    totallines = 0
    with open(csvfile,"r") as file:
        reader = csv.reader(file)
        totallines = sum(1 for row in reader)
    print(totallines)
    if totallines > 20:
        line = totallines - 20
    else:
        line = 3
    return line

def save_to_csv(current_date):
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    filename = f"{current_date}.csv"
    csv_file_path = "test_Alldatas.csv"

    folder_id = '1ztWIVXy_3z2zNlTQaRnAoLNic0QcYZHR'
    gfile = drive.CreateFile({'title': filename, 'parents': [{'id': folder_id}], 'mimeType': 'text/csv'})

    # Read the CSV data from the file and directly upload it
    with open(csv_file_path, 'r') as csvfile:
        csv_data = csvfile.read()
        gfile.SetContentString(csv_data)
        gfile.Upload()
    return

def main():
    save_to_csv()


if __name__ == "__main__":
    main()
import random as rng
import csv
import time
csvfile = "Alldatas.csv"

def DataGeneration(Temperature, Humidity, Moisture_sensor, Potentiometer, LDR):
    Time = (time.time() + 28800000) * 1000
    WriteData([Time, Temperature, Humidity, Moisture_sensor, Potentiometer, LDR])
    return [Time, Temperature, Humidity, Moisture_sensor, Potentiometer, LDR]

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